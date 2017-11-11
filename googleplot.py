import psycopg2
import gmplot

# Connect to the database
#db_conn = psycopg2.connect("dbname='test' host='127.0.0.1' user='root' password=''")

#Set the cursor
#cur = db_conn.cursor()

# Execute the database query. I am fetching business locations in a particular zip.
#cur.execute("select latitude, longitude from business where postal_code='89109';")

# Fetch all the data returned by the database query as a list
#lat_long = cur.fetchall()
lat_long =[][]
lat_long.append(1,1);
lat_long.append(1,2);
lat_long.append(1,3);
lat_long.append(2,1);
lat_long.append(3,1);
lat_long.append(3,2);
# Initialize two empty lists to hold the latitude and longitude values
latitude = []
longitude = [] 

# Transform the the fetched latitude and longitude data into two separate lists
for i in range(len(lat_long)):
	latitude.append(lat_long[i][0])
	longitude.append(lat_long[i][1])

# Initialize the map to the first location in the list
gmap = gmplot.GoogleMapPlotter(latitude[0],longitude[0])

# Draw the points on the map. I created my own marker for '#FF66666'. 
# You can use other markers from the available list of markers. 
# Another option is to place your own marker in the folder - 
# /usr/local/lib/python3.5/dist-packages/gmplot/markers/
gmap.scatter(latitude, longitude, '#FF6666', edge_width=10)

# Write the map in an HTML file
gmap.draw('map.html')

# Close the cursor and the database connection 
cur.close()
db_conn.close()