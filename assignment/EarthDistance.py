import math

radius = 6371.01

latitudeA = float(input("Input the latitude of coordinate 1: "))
longitudeA = float(input("Input the longitude of coordinate 1: "))
latitudeB = float(input("Input the latitude of coordinate 2: "))
longitudeB = float(input("Input the longitude of coordinate 2: "))

latitudeA = math.radians(latitudeA)
longitudeA = math.radians(longitudeA)
latitudeB = math.radians(latitudeB)
longitudeB = math.radians(longitudeB)

distance = radius * math.acos(math.sin(latitudeA) * math.sin(latitudeB) + math.cos(latitudeA) * math.cos(latitudeB) * math.cos(longitudeA - longitudeB))

print("The distance between those points is:", distance, "km")
