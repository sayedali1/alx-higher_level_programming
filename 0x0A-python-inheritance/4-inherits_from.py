#!/usr/bin/python3
#!/usr/bin/python3
"""
Moudle-4: inherits_from
contain one public method
"""

def inherits_from(obj, a_class):
    """
    if the object is an instance of a class that
    inherited (directly or indirectly)from the specified class
    """
    return type(obj) != a_class 
