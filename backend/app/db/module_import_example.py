from dotenv import load_dotenv
import os
import sys
from app.api.example1 import example1func
from app.db.example2 import example2func

def import_module_from_another_package():
    load_dotenv()
    pythonpath = os.getenv('PYTHONPATH')    
    print(f"PYTHONPATH is set to: {pythonpath}")
    if pythonpath:
        sys.path.append(pythonpath)
    example1func()

def import_module_from_the_same_package():
    example2func()

if __name__ == "__main__":
    import_module_from_another_package()
    import_module_from_the_same_package()