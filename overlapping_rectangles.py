from collections import namedtuple

Rectangle = namedtuple('Rectangle', 'top right bottom left')

def area_of_overlapping_rectangles(r1, r2):
    width = min(r1.right, r2.right) - max(r1.left, r2.left)
    height = min(r1.top, r2.top) - max(r1.bottom, r2.bottom)

    return width * height if width > 0 and height > 0 else 0

r1 = Rectangle(5, 5, 1, 2)
r2 = Rectangle(7, 5, 2, 3)

print(area_of_overlapping_rectangles(r1, r2))

r1 = Rectangle(5, 4, 1, 2)
r2 = Rectangle(7, 6, 2, 5)

print(area_of_overlapping_rectangles(r1, r2))
