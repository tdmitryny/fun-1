import math


def paint_calc(height,width,cover ):
       area = height * width
       num_of_can = math.ceil(area / cover)
       print(f"You need {num_of_can} cans ")

test_w = int(input("Width of wall: "))
test_h = int(input("Height of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover = coverage)
