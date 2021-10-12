import csv
import numpy as np
import pandas as pd
import numpy as np
import folium
from folium import plugins
import sys
import googlemaps
from datetime import datetime
from sklearn.neighbors import BallTree
sys.setrecursionlimit(10**8)



with open('/Data/AED_Final_Final.csv', encoding='euc-kr') as csvfile:
  csvreader = csv.reader(csvfile)
  next(csvreader)
  rows = []
  for row in csvreader:
    rows.append(row[-3:])
b = []
for i in range(len(rows)):
  b.append(rows[i][1:])
c = np.array(b,dtype='float32')
d = c.tolist().copy()




def getLoc(addr):
    gmaps = googlemaps.Client(key='AIzaSyC4aSm3hOBTab0Gw9iHsUV6ffqitwk702s')
    geocode_result = gmaps.geocode(addr)
    n_lat = geocode_result[0]['geometry']['location']['lat']
    n_lng = geocode_result[0]['geometry']['location']['lng']
    loc = n_lat, n_lng
    return loc
get_location = getLoc(input("장소를 입력해주세요 : "))

# input 사용해서서 구현해보기
print("현재 위치 : ", get_location)


def lo_index(x,y):
  final = np.array(d, dtype='float32')
  tree = BallTree(final)
  dist, ind = tree.query([np.array(get_location, dtype='float32')], 5)
  near_location_index = ind.tolist()
  near_location_index_row = near_location_index[0]
  return near_location_index_row

location_index = lo_index(x=d, y=get_location)
wow = []
for i in range(len(location_index)):
  wow.append(d[location_index[i]])



my_map_f = folium.Map(location=get_location, tiles='OpenStreetMap',zoom_start=15)
folium.Marker(location=get_location, popup='<p>현재위치<p>', tooltip='현재위치', icon=folium.Icon(color='red')).add_to(my_map_f)
folium.CircleMarker(get_location, popup='<i>반경</i>', radius = 200, color = '#00FF00', fill_color = '#00FF00', fill=True ).add_to(my_map_f)
for x, y in wow:
  my_marker = folium.Marker(location=[x, y], tooltip='AED').add_to(my_map_f) # popup=z 빠짐

my_map_f