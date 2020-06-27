"""
Created in April, 2020
@author: Wjdan Alharthi (wjdanalharthi)
"""

import json
import requests


# hardcoded names and OSM ID's of all Saudi Arabian regions
REGIONS_OSM_CODES = \
        {'Qassim':'3679872',
        'Riyadh':'3678409',
        'Tabuk':'3679867',
        'Madinah':'3679869',
        'Makkah':'3678639',
        'Northern Region':'3673927',
        'Jawf':'3842543',
        'Hail':'3676707',
        'Bahah':'3679888',
        'Jizan':'3679903',
        'Asir':'3678598',
        'Najran':'3667317',
        'Eastern Region':'3667294'}


# prepare output as JSON
output = dict([('type', 'FeatureCollection'), ('features', [])])


# prepare http header
header = {'User-Agent': 'Mozilla/5.0'}
for k in REGIONS_OSM_CODES:

        # build the URL and get data on region k
        url = "https://nominatim.openstreetmap.org/reverse?osm_type=R&osm_id=%s&format=json&polygon_geojson=1" % REGIONS_OSM_CODES[k]
        r = requests.get(url)
        data = r.json()

        # exctract information and add to output
        feature = dict([('type', 'Feature'), ('properties', dict()), ('geometry', dict())])
        feature['properties']['name'] = k
        feature['geometry']['type'] = data['geojson']['type']
        feature['geometry']['coordinates'] = data['geojson']['coordinates']

        output['features'].append(feature)

# dump output in json file
with open('./data/SA_regions.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
