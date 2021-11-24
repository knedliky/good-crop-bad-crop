'''
A module for creating the leaflet mapping layer
'''

import dash_leaflet as dl
import os
from map_functions import *
from rasterio import features

API_KEY = os.environ['API_KEY']


def create_map(lat, lon):
    
    t = dl.TileLayer(
        url = 'https://api.tiles.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}.png?access_token=' + API_KEY,
        attribution = '&copy; boii.io',
    )

    m = dl.Map(
        zoom = 14,
        location_lat_lon_acc = get_centroid(lat,lon),
        children = [t]
    )


    return m



def _create_map(lat, lon):

    left, bottom, right, top = features.bounds(get_aoi(lat,lon))
    bounds = ([bottom, right], [top, left])


    m = dl.Map(
        location = get_centroid(lat,lon),
        tiles = None,
        zoom_start = 14
        )


    dl.TileLayer(
    name = 'Basemap',
    tiles = 'https://api.tiles.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}.png?access_token=' + API_KEY,
    attr = 'MapBox',
    overlay = False
    ).add_to(m)


    return m


if __name__ == '__main__':
    print('This should not be run')