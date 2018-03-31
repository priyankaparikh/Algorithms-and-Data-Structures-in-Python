def merge_sort(lst):
    """Merge sort an input list"""

    if len(lst) < 2:
        return list

    # choose a pivot index
    mid = int( len(lst) / 2)
    lst1 = merge_sort(lst[:mid]) # O(n)
    lst2 = merge_sort(lst[mid:])

    return make_merge(lst1, lst2)

def make_merge(lst1, lst2):
    """ Merge lists """

    result_list = []

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
