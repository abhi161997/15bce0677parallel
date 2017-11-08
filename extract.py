import MySQLdb
import math
import multiprocessing

from math import cos, asin, sqrt

#calculating distance between two coordinates on earth
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

#equation to check whether the city lies in the shortest path equation between the graph line
#using the distance between two latidinal and lonigitudinal points
#point to check for has coodinates(x,y)
#source and destination is (x1,y1) and (x2,y2)
def pathequation(x,y,x1,y1,x2,y2):
    p = ((y-y1)-((y2-y1)/(x2-x1))*(x-x1))
    if p>=-1 and p<=1:
        return 1
    else:
        return 0

x = 1
y = 1
x1 = 2
y1 = 2
x2 = 3
y2 = 3

result = pathequation(x,y,x1,y1,x2,y2)
print(result)
