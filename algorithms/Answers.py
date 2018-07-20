# Exercise II
# a.


def a_max_difference(arr):
    i = arr[0]
    j = arr[1]

    for x in range(2, len(arr)):
        if arr[x - 1] < i:
            i = arr[x - 1]
        if arr[x] > j:
            j = arr[x]

    return j - i


def b_broken_eggs(floors, f):
