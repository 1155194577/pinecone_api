from app.api.example1 import example1func
from app.db.example2 import example2func
from app.util.load_abs_path import load_abs
def import_module_from_another_package():
    example1func()

def import_module_from_the_same_package():
    example2func()

if __name__ == "__main__":
    load_abs()
    import_module_from_another_package()
    import_module_from_the_same_package()