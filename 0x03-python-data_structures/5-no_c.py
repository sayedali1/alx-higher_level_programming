#!/urs/bin/python3
def no_c(my_string):
    # covert str into list
    list_str = [ch for ch in my_string if ch not in 'cC']
    # conver list into str
    new_str = ""
    for ch in list_str:
        new_str = new_str + ch
    return new_str
