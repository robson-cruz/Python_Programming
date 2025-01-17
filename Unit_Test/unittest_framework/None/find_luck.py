# this code is in the find_luck.py file
import re


def find_luck(string):
    """ Check if a given string contains the word luck """
    if re.findall("luck", string):
        return 'luck'
    else:
        return None
