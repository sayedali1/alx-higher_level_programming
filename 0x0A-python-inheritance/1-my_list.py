#!/usr/bin/python3

"""
Moudle-1: Mylist

inhirts from a list,
contain public method that sort list
"""


class MyList(list):
    """ inherts from a list"""

    def print_sorted(self):
        """ fun that sort the list in asending order """
        return print(sorted(self))
