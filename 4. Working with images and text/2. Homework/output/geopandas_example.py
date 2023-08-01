import geopandas as gpd

# Rest of your code using geopandas
# For example, you can read a shapefile and display its contents:
data = gpd.read_file('path_to_your_shapefile.shp')
print(data.head())