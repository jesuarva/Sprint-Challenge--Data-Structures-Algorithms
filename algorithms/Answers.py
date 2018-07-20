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


# b.
import math


def b_broken_eggs(floors, f):
    steps = 0
    control = floors
    broken_eggs = 0

    def jump(direction):
        floors_to_jump = math.ceil(floors * (2**steps))
        if direction == 1:
            control += floors_to_jump
        elif direction == 0:
            control -= floors_to_jump

    while control > 0:
        steps += 1
        if control == f:
            broken_eggs += 1
            return control, broken_eggs
        elif control > f:
            broken_eggs += 1
            jump(1)
        else:
            jump(0)
