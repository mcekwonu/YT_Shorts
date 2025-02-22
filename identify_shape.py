#
# www.youtube.com/@mersthub_mentors
#


def identify_shape(sides):
    match sides:
        case 3:
            return "Triangle"
        case 4:
            return "Quadrilateral"
        case 5:
            return "Pentagon"
        case 6:
            return "Hexagon"
        case 7:
            return "Heptagon"
        case 8:
            return "Octagon"
        case 9:
            return "Nonagon"
        case _:
            return "Unknown shape"


print(identify_shape(sides=15), end="\n")
print(identify_shape(sides=6))
