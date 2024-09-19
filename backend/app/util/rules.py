import re
def is_valid_index_name(index_name):
        # "Name must consist of lower case alphanumeric characters or '-'"
        pattern = r'^[a-z0-9-]+$'
        return re.match(pattern, index_name) is not None

def is_valid_namespace_name(namespace_name):
        # "Name must consist of lower case alphanumeric characters or '-'"
        pattern = r'^[a-z0-9-]+$'
        return re.match(pattern, namespace_name) is not None    