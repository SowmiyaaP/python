import math
def paint(height,width,cover):
    paint =( height * width) / cover
    print(math.ceil(paint))

h =  float(input("Enter the height: "))
w = float(input("Enter the width: "))
coverage = 5
paint(h,w,coverage)   

