#!/urs/bin/python3
def no_c(my_string):
    new_str = "".join(c for c in my_string if c not in "cC")
    return new_str
