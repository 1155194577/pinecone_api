from typing import List   
def get_keys_from_dict(d)-> List:
    return [key for key in d]   

def get_values_from_dict(d)->List:
    return [d[key] for key in d]