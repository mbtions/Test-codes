import math

def two_point_slope_form(point1, point2):
    if point1[0] == point2[0]:
        # The line is vertical.
        return None, None, None, f"The line is vertical: x = {point1[0]}"
    
    # Calculate the slope (m)
    m = (point2[1] - point1[1]) / (point2[0] - point1[0])
    
    # Convert to general form: Ax + By + C = 0
    A = -m
    B = 1
    C = -(point1[1] - m * point1[0])
    
    return A, B, C #, f"y - {point1[1]} = {m}(x - {point1[0]})"

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
    
def mirror_image_of_point(point, A, B, C):
    # Step 1: Calculate the perpendicular projection (x2, y2) of (x1, y1) on the line.
    denominator = A**2 + B**2
    x2 = (B * (B * point[0] - A * point[1]) - A * C) / denominator
    y2 = (A * (A * point[1] - B * point[0]) - B * C) / denominator

    # Step 2: Calculate the mirror image (x', y') using midpoint formula.
    x_prime = 2 * x2 - point[0]
    y_prime = 2 * y2 - point[1]

    return x_prime, y_prime

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
    
def find_intersection(A1, B1, C1, A2, B2, C2):
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

# Input 
area = int(input())
side = math.sqrt(area)

p, q, r, s = map(int, input().split(" "))
points = [
    (0, 0), 
    (0, side),
    (p, q),
    (side, 0),
    (r, s),
    (side, side)
]

countpoints = 0
new_points = []
original_points = []
more_points = []

if (p==r):
    if (p > side/2):
        new_points = [(p,q), (r,s), (2*p, q), (2*p, s)]
    else:
        new_points = [(p, q), (r,s), (side, 0), (side, side)]
elif (q==s):
    if (q < side/2):
        new_points = [(p,q), (r,s), (p, -(side-2*q)), (r, -(side-2*s))]
    else:
        new_points = [(p,q), (r,s), (0,0), (side, 0)]
else:
    A,B,C = two_point_slope_form((p, q), (r, s))

    for point in points:
        position = is_point_above_line(point, A, B, C)
        if (position == "above"):
            x_mirror, y_mirror = mirror_image_of_point(point, A, B, C)
            new_points.append((round(x_mirror, 2), round(y_mirror, 2)))
        else: 
            original_points.append(point)

if (len(new_points) > 1):
    
    A1, B1, C1  = two_point_slope_form((p, q), new_points[0])
    A2, B2, C2 = two_point_slope_form(new_points[1], (r, s))
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
for point in original_points:
    all_points.append(point)
# all_points.append((p, q))
# all_points.append((r, s))

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