#
# www.youtube.com/@mersthub_mentors
#

from functools import partial


def multiply(x, y):
    return x * y,


multiply_by_six = partial(multiply, 6)

print(multiply_by_six(20))
