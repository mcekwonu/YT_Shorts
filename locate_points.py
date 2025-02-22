#
# www.youtube.com/@mersthub_mentors
#


def locate_points(point):
    x, y = point
    match point:
        case (0, 0):
            print("This is the origin")
        case (x, 0):
            print(f"Point is on x-axis at {x}")
        case (0, y):
            print(f"Point is on the y-axis at {y}")
        case _:
            print(
                f"Point is at coordinates ({x}, {y})")


locate_points((12, -2))
# Output: Point is at coordinates (12, -2)

locate_points((0, 0))
# Output: This is the origin

locate_points((-5, 0))
# Output: Point is on the x-axis at -5
