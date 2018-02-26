import folium
import pandas
import json
import io

#Reading data from the file which contains comma separated values
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data['LAT'])				#Latitutde for plotiing the points
lon = list(data['LON'])				#Longitude for plotting the points
name = list(data['NAME'])			#Name for the popup value
location = list(data['LOCATION'])	#Location for the popup value
elev = list(data['ELEV'])			#Elevation for the popup color

#Function to decide the color of the point based on the elevation value
def color_picker(el):
	if el < 1500:
		return "green"
	elif 1500 <= el < 3000:
		return "orange"
	else:
		return "red"

#Create a Map object using the folium library based on the following properties
webmap = folium.Map(location=[48.7767982,-121.8109970], zoom_start=6, tiles="Mapbox Bright")

#Create a point layer for plotting the volcano locations using feature groups
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, nm, loc in zip(lat, lon, elev, name, location):
 	fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(nm + ", " + loc, parse_html=True), icon=folium.Icon(color=color_picker(el))))

#Create a polygon layer for outlining the diferent countries of the world using feature groups
fgp = folium.FeatureGroup(name="Population")
file = json.load(io.open("world.json",'r', encoding='utf-8-sig'))
#Fill the contries with different colors based on their population --> see the style_function property
fgp.add_child(folium.GeoJson(file, style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

#Add both the layers(feature groups) to the webmap
webmap.add_child(fgv)
webmap.add_child(fgp)
webmap.add_child(folium.LayerControl())		#Adding layer control in the webmap for turning the individual layers on/off 
webmap.save("webmaps.html")