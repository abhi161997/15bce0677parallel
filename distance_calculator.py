from math import cos, asin, sqrt

#calculating distance between two coordinates on earth
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

lat1 = float(input("Enter value of Latitude 1"))
long1 = float(input("Enter value of longitude 1"))
lat2 = float(input("Enter value of latitude 2 "))
long2 = float(input("Enter value of longitude 2 "))

d = distance(lat1,long1, lat2, long2)
print(d)
