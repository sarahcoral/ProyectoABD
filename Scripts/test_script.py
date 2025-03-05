def do_something():
    print("test script loaded!")

from pathlib import Path
address = Path.cwd()
print(address)