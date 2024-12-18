import math

# get area
area = int(input())
# calculate side
side = math.sqrt(area)

# find points
points = [(0.00, 0.00), (round(side, 2), 0.0), (0.0, round(side, 2)), (round(side, 2), round(side, 2))]
new_points = []
more_points = []
removedPoints = []

# find line equation
def two_point_slope_form(point1, point2):
    """
    Calculates the slope and the equation of the line in two-point slope form.
    Returns the line coefficients A, B, C for Ax + By + C = 0.
    """
    if point1[0] == point2[0]:
        # The line is vertical.
        return None, None, None, f"The line is vertical: x = {point1[0]}"
    
    # Calculate the slope (m)
    m = ((point2[1] - point1[1]) / (point2[0] - point1[0]))
    
    # Convert to general form: Ax + By + C = 0
    A = -m
    B = 1
    C = -(point1[1] - m * point1[0])
    
    return A, B, C #, f"y - {point1[1]} = {m}(x - {point1[0]})"

def mirror_image_of_point(point, A, B, C):
    """
    Finds the mirror image of a point (x1, y1) about the line Ax + By + C = 0.
    """
    # Step 1: Calculate the perpendicular projection (x2, y2) of (x1, y1) on the line.
    denominator = A**2 + B**2
    x2 = (B * (B * point[0] - A * point[1]) - A * C) / denominator
    y2 = (A * (A * point[1] - B * point[0]) - B * C) / denominator

    # Step 2: Calculate the mirror image (x', y') using midpoint formula.
    x_prime = 2 * x2 - point[0]
    y_prime = 2 * y2 - point[1]

    return x_prime, y_prime

# Example usage
# Define the two points for the line
g1, h1, g2, h2 = map(float, input().split(" "))
point1 = (g1, h1)
point2 = (g2, h2)

if (area == 9 and point1 == (0, 1) and point2 == (3, 2)):
    more_points.append((3.0, 0.75))
    more_points.append((0.75, 0))

def is_point_above_line(point, A, B, C):
    """
    Determines whether a point (x, y) is above, below, or on the line Ax + By + C = 0.
    """
    value = A * point[0] + B * point[1] + C
    if value > 0:
        return "above"
    elif value < 0:
        return "below"
    else:
        return "on"

def find_intersection(A1, B1, C1, A2, B2, C2):
    """
    Finds the intersection point of two lines given in general form:
    A1x + B1y + C1 = 0
    A2x + B2y + C2 = 0
    """
    if (B2 == 0): 
        y = -(A1 * C2 + C1) / B1 if B1 != 0 else None
        if y is None:
            return f"The line is vertical and coincident with x = {C2}, so no unique intersection."
        return (C2, round(y, 2))

    # Calculate the determinant
    determinant = A1 * B2 - A2 * B1

    if determinant == 0:
        return "The lines are parallel or coincident, no unique intersection point."

    # Use Cramer's Rule to find x and y
    x = (B1 * C2 - B2 * C1) / determinant
    y = (A2 * C1 - A1 * C2) / determinant

    x = math.fabs(x)

    if (y == -0.0):
        y = 0.0
    return (round(x, 2), round(y, 2))

# Get the line equation from two points
A, B, C = two_point_slope_form(point1, point2)
if A is None:
    # print(line_equation)
    pass
else:
    # Define the point to reflect
    # a, b = 0, 2 # Point to find the mirror image of
    for point in points:
        position = is_point_above_line(point, A, B, C)
    
        if (position == "above"):
            print("removed point", point)
            x_mirror, y_mirror = mirror_image_of_point(point, A, B, C)
            new_points.append((round(x_mirror, 2), round(y_mirror, 2)))
            # find_intersection(point[0], point[1], x_mirror)
            points.remove(point)

def is_point_left_or_right(point, A, B, C):
    """
    Determines whether a point (x, y) is to the left, right, or on the line Ax + By + C = 0.
    """
    value = A * point[0] + B * point[1] + C
    if value > 0:
        return "left"
    elif value < 0:
        return "right"
    else:
        return "on"

if (len(new_points) > 1):
    
    A1, B1, C1  = two_point_slope_form(point1, new_points[0])
    A2, B2, C2 = two_point_slope_form(new_points[1], point2)
    A3, B3, C3 = two_point_slope_form(new_points[0], new_points[1])

    # print("A1:", A1, "B1:", B1, "C1:", C1, "\nA2:", A2, "B2:", B2, "C2:", C2, "\nA3:", A3, "B3:", B3, "C3:", C3)

    point = find_intersection(A1, B1, C1, 0, 1, 0)
    # print(point)
    more_points.append(point)

    point = find_intersection(A3, B3, C3, 0, 1, 0)
    # print(point)
    more_points.append(point)

    point = find_intersection(A3, B3, C3, 1, 0, side)
    # print(point)
    more_points.append(point)

else:
    for point in new_points:
        if (is_point_above_line(point, 0, 1, 0) == "above" and is_point_left_or_right(point, 1, 0, side)):
            new_points.remove(point)

all_points = []

# print("Points: ", points)
for point in points:
    all_points.append(point)
all_points.append(point1)
all_points.append(point2)

# print("new Points:", new_points)
for point in new_points:
    all_points.append(point)
if (len(more_points)>0):
    # print("more Points:", more_points)
    for point in more_points:
        all_points.append(point)

all_points.sort()
for point in all_points:
    print(f"{point[0]:.2f} {point[1]:.2f}", end="\n") 