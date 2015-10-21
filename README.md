# jrdata
Jízdní řády z Dopravního podniku hlavního města Praha

Staženo z FTP serveru Dopravního podniku

ftp://ftp.dpp.cz/

jrdata
jrdata15

## Původní zdroj

@datastory
https://datastory.cz/dpp/foia/2015/10/20/informace-zpusobuji-silenstvi.html

## Převod na GeoJSON pro zobrazení v mapě

1. Přejmenovat `soubor.txt` na `soubor.csv`
2. vytvořit soubor `*.vrt`, kterým popíšte vstupní CSV soubor::
```xml 
    <OGRVRTDataSource>
            <OGRVRTLayer name="stops">
                <SrcDataSource>orig-data/stops.csv</SrcDataSource>
                <GeometryType>wkbPoint</GeometryType>
                <LayerSRS>WGS84</LayerSRS>
                <GeometryField encoding="PointFromColumns" x="stop_lon" y="stop_lat"/>
            </OGRVRTLayer>
    </OGRVRTDataSource>
```

3. ogr2ogr -f GeoJSON json/stops.geojson vrts/stops.vrt

výsledek: https://github.com/jachym/jrdata/blob/master/jsons/stops.geojson


## Převod shapes.txt na GeoJSON a zobrazení v mapě

1. vezmi skript v `bin/shapes2geojson.py`
2. Použij

```Bash

python3 bin/shapes2geojson.py > jsons/shapes.geojson

```

Viz https://github.com/jachym/jrdata/blob/master/jsons/shapes.geojson

