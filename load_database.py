def load_db():
    import os
    import requests
    
    #file_path = Path.cwd(),r"linkedindatabase.db")
    file_path = r"linkedindatabase.db"
    
    if not os.path.exists(file_path):
        print('Database not ready. Loading...')
        try:
            # URL of your Google Drive database file (direct download link)
            url = "https://drive.google.com/uc?id=1e_PSowuukgifVA7rzqkvhDuCud-YDxtN"
            # Send a GET request to download the file
            response = requests.get(url)
            # Save the content to a local file (in the Binder container or local disk)
            with open('linkedindatabase.db', 'wb') as f:
                f.write(response.content)
            print("Database available!")
            return 1
        except Exception as e:
            print("Failed to fetch database: {e}")
            return 0
    else:
        print('Database already loaded!')
        return 2