import pandas as pd
import simplekml

df = pd.read_csv("LUCAS-SOIL-2018.csv")
df = df[(df["NUTS_0"]=="ES") & (df["NUTS_1"]=="ES4")&(df["NUTS_2"]=="ES41") & (df["NUTS_3"]=="ES418")]
lats = list(df["TH_LAT"])
longs = list(df["TH_LONG"])
print(len(lats))
coordinates = []

for i in range(len(lats)):
    coordinates.append((lats[i], longs[i]))

min_lat, min_lon = min(coordinates, key=lambda x: x[0])[0], min(coordinates, key=lambda x: x[1])[1]
max_lat, max_lon = max(coordinates, key=lambda x: x[0])[0], max(coordinates, key=lambda x: x[1])[1]

kml = simplekml.Kml()
polygon = kml.newpolygon(name="Bounding Rectangle",
                         outerboundaryis=[(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat),
                                          (min_lon, max_lat), (min_lon, min_lat)])

kml.save("kml_es.kml")