def slope_and_y_intercept(pos1, pos2):
    slope = (pos2[1] - pos1[1]) / (pos2[0] - pos1[0])
    y_intercept = pos2[1] - slope * pos2[0]

    return (slope, y_intercept)

print(slope_and_y_intercept((1, 2), (2, 4)))

def find_points_above_a_line(points, slope, y_intercept):
    return [point for point in points if point[1] > slope * point[0] + y_intercept]


def find_points_below_a_line(points, slope, y_intercept):
    return [point for point in points if point[1] < slope * point[0] + y_intercept]

points = [(2, 5), (1, 3), (3, 2), (5, 5), (0, 2), (4, 5)]

print(find_points_above_a_line(points, *slope_and_y_intercept((1, 2), (2, 4))))

def find_line_that_divides(points):
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            slope, y_intercept = slope_and_y_intercept(points[i], points[j])
            
            if len(find_points_above_a_line(points, slope, y_intercept)) == len(find_points_below_a_line(points, slope, y_intercept)):
                return (points[i], points[j])

print(find_line_that_divides(points))
