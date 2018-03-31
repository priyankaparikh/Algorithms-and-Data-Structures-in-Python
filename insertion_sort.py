""" Insertion sort is a simple sorting algotrithm.
    It has quadratic run time O(N2).
    It is an adaptive, in- place, online algorithm.
"""

def insertion_sort(lst):
    """ given a list , sort using insertion sort"""

    for i in range(1, len(lst)):
        j = i - 1

        while j >= 0 and lst[j] > lst[i]:
            j -= 1

        j += 1

        if j != i :
            lst[j:i + 1] = lst[i:i + 1] + lst[j:1]

    return lst

if __name__ == "__main__":

    num = [5, 2, 1, 7, 6, 88, 0]

    print (insertion_sort(num))
