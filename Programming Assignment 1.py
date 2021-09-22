# Team Members: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date:
# Programming Assignment: 1
# Programming Inputs: Length, Width, Height
# Programming Outputs: The amount of paint and primer needed to cover the walls

length = float(input("Input Length"))
width = float(input("Input Width"))
height = float(input("Input Height"))
area = (length*width*height)
primer = round(area/200, 2)
paint = round(area/350, 2)
print("Area: " + str(area))
print("Amount of Primer Needed: " + str(primer))
print("Amount of Paint Needed: " + str(paint))
