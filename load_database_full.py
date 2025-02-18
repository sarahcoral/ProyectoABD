def load_db(given_project_folder=None):
    from pathlib import Path
    import requests
    import json
    
    #SET PROJECT FOLDER MAIN DIRECTORY
    if given_project_folder == None:
        project_folder = Path.cwd()
    else:
        project_folder = given_project_folder
    print(f"Project folder set to {project_folder} for load_database.py")
    
    #LOAD LOCAL_SETUP_CONFIG FILE
    config_path = project_folder / "local_setup_config.json"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as file:
            local_config  = json.load(file)
    else:
        raise FileNotFoundError(f"Error: {config_path} not found")
    
    # set run_local
    run_local = local_config["run_local"]

    #set path for database file
    if not run_local:
        database_file_path = project_folder / "database" / "linkedindatabase.db"
    else:
        print("You're running on local")
        database_file_path = project_folder / "database" / "linkedindatabase.db"

    
    #create or open linkedindatabase.db, connect to it and create a cursor object
    if not database_file_path.exists():
        print('Database not ready. Loading...')
        try:
            # URL of your Google Drive database file (direct download link)
            url = "https://www.googleapis.com/drive/v3/files/1e_PSowuukgifVA7rzqkvhDuCud-YDxtN?alt=media&key=AIzaSyDgoIBvsODQNReD8hl8DiACY2ntGbc5wYc"
            # Send a GET request to download the file
            response = requests.get(url)
            # Save the content to a local file (in the Binder container or local disk)
            with open('linkedindatabase.db', 'wb') as f:
                f.write(response.content)
            print("Database available!")
        except Exception as e:
            print("Failed to fetch database: {e}")
    else:
        print('Database already loaded!')