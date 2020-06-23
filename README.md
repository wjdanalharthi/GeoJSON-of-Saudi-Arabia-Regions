# GeoJSON of Saudi Arabia Regions
A script that builds a GeoJSON of Saudi Arabia goveranates with an demostration

## Motivation
I wanted to created a heatmap of Saudi Arabia such that the variation in color is indicated by the data point in my dataset, such as the example picture below
![alt text](https://www.researchgate.net/profile/Hala_Elmorshedy/publication/282947082/figure/fig7/AS:285973712785414@1445192854943/Kingdom-of-Saudi-Arabia-map-showing-the-13-provinces-From-mapsopensourcecom_Q320.jpg)

Such visualization requires us to know the latitude and longitude of every point on the boundaries of each region. In other words we need the exactly geographic encoding of the regions, which we call ![GeoJson](GeoJson.org).
 
One way to do is manually drawing the boundaries using tools such as ![geojson.io](geojson.io), and exporting the GeoJSON data. An easier way is to utilize OpenStreetMaps to obtain that data. 

In this repo I write a script that queries the GeoJson data of all regions of Saudi, and demonstrated it on the map using `folium` visualization library. 
