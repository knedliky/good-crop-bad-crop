'''
A module containing the mapping and tiling functions need to render the leaflet map
'''
import geopandas as gpd
from pathlib import Path
import json

DATA_PATH = Path.cwd().joinpath('data')

# returns an area of interest as a GeoPandas object
def get_aoi(lat, lon):
    return gpd.read_file(f'{DATA_PATH}/geometries/geo-x{lat}-y{lon}.geojson')


# returns the centroid of an area, in the form (lon, lat)
def get_centroid(lat, lon):
    [[x1, y1], [x2, y2]] = get_bounds(lat, lon)
    return [(x1 + x2)/ 2, (y1 + y2) / 2]


# returns the south-east and north west corner of a tile
def get_bounds(lat, lon):
    with open(f'{DATA_PATH}/geometries/geo-x{lat}-y{lon}.geojson') as f:
        coordinates = json.load(f)['features'][0]['geometry']['coordinates']
        lon_min = coordinates[0][1][0]
        lat_min = coordinates[0][1][1]
        lon_max = coordinates[0][3][0]
        lat_max = coordinates[0][3][1]
        return [[lat_min, lon_min], [lat_max, lon_max]]


if __name__ == '__main__':
    print('Do nothing')