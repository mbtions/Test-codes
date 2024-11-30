import math

area = int(input())
side = math.sqrt(area)

points = [(0.0,0.0), (round(side, 2), 0.0), (0.0, round(side, 2)), (round(side, 2), round(side, 2))]
new_points = []

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
    
    return A, B, C, f"y - {point1[1]} = {m}(x - {point1[0]})"

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
# x1_line, y1_line = 1, 2  # First point on the line
# x2_line, y2_line = 4, 6  # Second point on the line
g1, h1, g2, h2 = map(int, input().split(" "))

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

removedPoints = []
# Get the line equation from two points
A, B, C, line_equation = two_point_slope_form((g1, h1), (g2, h2))
if A is None:
    print(line_equation)
else:
    print("The equation of the line in two-point slope form is:")
    print(line_equation)

    # Define the point to reflect
    # a, b = 0, 2 # Point to find the mirror image of
    for point in points:
        position = is_point_above_line(point, A, B, C)
    
        if (position == "above"):
            print("removed point", point)
            x_mirror, y_mirror = mirror_image_of_point(point, A, B, C)
            new_points.append((round(x_mirror, 2), round(y_mirror, 2)))
            # removedPoints.append(point)
            points.remove(point)

print(new_points)
more_points = []

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

A1, B1, C1, line_equation1 = two_point_slope_form((g1, h1),new_points[0])
A2, B2, C2, line_equation2 = two_point_slope_form(new_points[1], (g2, h2))
A3, B3, C3, line_equation3 = two_point_slope_form(new_points[0], new_points[1])

print("A1:", A1, "B1:", B1, "C1:", C1, "\nA2:", A2, "B2:", B2, "C2:", C2, "\nA3:", A3, "B3:", B3, "C3:", C3)

point = find_intersection(A1, B1, C1, 0, 1, 0)
print(point)
more_points.append(point)

point = find_intersection(A3, B3, C3, 0, 1, 0)
print(point)
more_points.append(point)

point = find_intersection(A3, B3, C3, 1, 0, side)
print(point)
more_points.append(point)

# more_points.append(find_intersection(A2, B2, C2, 1, 0, side))

print(more_points)

# all_points = []
# for point in points:
#     if point in removedPoints:
#         points.remove(point)

for point in points:
    all_points.append(point)
all_points.append((g1, h1))
all_points.append((g2,h1))
for point in new_points:
    all_points.append(point)
if (len(more_points)>0):
    for point in more_points:
        all_points.append(point)

all_points.sort()
print(all_points)