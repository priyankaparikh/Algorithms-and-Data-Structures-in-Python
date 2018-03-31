def simplify(s):
    """simplify split sqaure """

    if type(s) == int:
        return s

    # simplify the nested lists in a list comprehension adn recursion
    lst = [simplify(item) for item in s]

    if lst == [0, 0, 0, 0] or lst === [1, 1, 1, 1]:
        return lst[0]

    else return lst
