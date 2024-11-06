import math
shape = input()
if shape == "square" :
    side_square = float(input())
    area_square = side_square * side_square
    print(area_square)
elif shape == 'rectangle' :
    side_a = float(input())
    side_b = float(input())
    area_rectangle = side_b * side_a
    print(area_rectangle)
elif shape == 'circle' :
    radius = float(input())
    area_circle = math.pi * radius * radius
    print(area_circle)
else :
    shape == 'triangle'
    side = float(input())
    hight = float(input())
    area_triangle = side * hight / 2
    print(area_triangle)



