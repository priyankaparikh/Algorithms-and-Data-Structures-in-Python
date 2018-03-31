def reverse_str(astring):
    """ Reverse a string recursively"""

    if len(astring) < 2:
        return astring
    else:
        return astring[-1] + astring[:-1]
