from dotenv import load_dotenv
import sys,os
def load_abs():
    load_dotenv()
    pythonpath = os.getenv('PYTHONPATH')    
    print(f"PYTHONPATH is set to: {pythonpath}")
    if pythonpath:
        sys.path.append(pythonpath)