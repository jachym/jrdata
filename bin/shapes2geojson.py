#!/usr/bin/env python3

# author: jachym
# licence: gpl3
# purpose: vyrobit použitelný data z bordelu od dpp

import csv, json

def makejson(reader):

    shapes = {}
    for rec in reader:
        shapeid = int(rec['shape_id'])
        if not shapeid in shapes:
            shapes[shapeid] = {
                'shape_id': shapeid,
                'coordinates': {
                }
            }
        seq = int(rec['shape_pt_sequence']) 
        shapes[shapeid]['coordinates'][seq] = [float(rec['shape_pt_lon']),
                                               float(rec['shape_pt_lat'])]
    fc = { "type": "FeatureCollection",
        "features": []
    }

    for shapeid in shapes:
        shape = shapes[shapeid]
        feature = {
            "type": "Feature",
            "geometry": {
              "type": "LineString",
              "coordinates": []
          },
        "properties": {
          "shape_id": shapeid
          }
        }

        for point in shape['coordinates']:
            feature['geometry']['coordinates'].append(shape['coordinates'][point])

        fc['features'].append(feature)

    return fc


if __name__ == '__main__':

    output_json = None
    with open('orig-data/shapes.txt', 'r') as csvfile:
        routesreader = csv.DictReader(csvfile)
        output_json = makejson(routesreader)

    print(json.dumps(output_json))
