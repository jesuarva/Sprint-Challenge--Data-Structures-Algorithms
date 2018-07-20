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
    top = floors
    bottom = 1
    control = math.ceil(floors_above / 2)
    broken_eggs = 0

    def jump_up():
        bottom = control
        floors_above = top - bottom
        control += math.ceil(floors_above / 2)

    def jump_down():
        top = control
        floor_below = top - bottom
        control -= math.ceil(floor_below / 2)

    while control > 0:
        steps += 1
        if control == f:
            broken_eggs += 1
            return control, broken_eggs
        elif control > f:
            broken_eggs += 1
            jump_up()
        else:
            jump_down()
