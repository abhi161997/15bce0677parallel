import MySQLdb
import math
import multiprocessing
import _thread

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


sql1 = "select * from statelist where city_id <= 250";
sql2 = "select * from statelist where city_id <= 500 and city_id>=251"
sql3 = "select * from statelist where city_id <= 750 and city_id>=501"
sql4 = "select * from statelist where city_id <= 100 and city_id>=751"




db1 = MySQLdb.connect("localhost","root","","parallel")
db2 = MySQLdb.connect("localhost","root","","parallel")
db3 = MySQLdb.connect("localhost","root","","parallel")
db4 = MySQLdb.connect("localhost","root","","parallel")

c1 = db1.cursor()
c2 = db2.cursor()
c3 = db3.cursor()
c4 = db4.cursor()


#prallelprocessing function to retrive data from database
def search(cursor, query):
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        lat = row[2]
        long = row[3]
        name = row[1]
        print(lat+long+name)



search(c1,sql1)
search(c2,sql2)
search(c3,sql3)
search(c4,sql4)

#time function to display when a thread started
def print_time(threadName, delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s: %s" % (threadName, time.ctime(time.time())))


#executing database search query using thread diving it into 4 subgroup and executing it in parallel
try:
    _thread.start_new_thread(search,(c1,sql1, ))
    _thread.start_new_thread(search,(c2,sql2, ))
    _thread.start_new_thread(search,(c3,sql3, ))
    _thread.start_new_thread(search,(c4,sql4, ))
except:
    print("Error: Unable to start thread")





