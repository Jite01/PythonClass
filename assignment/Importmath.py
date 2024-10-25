import math

no = int(input("Input the number of sides on the polygon: "))
sides = float(input("Input the length of one of the sides: "))

area = (no * sides**2) / (4 * math.tan(math.pi / no))

print("The area is:", area)
