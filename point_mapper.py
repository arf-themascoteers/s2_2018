import pandas as pd
import rasterio


df = pd.read_csv("LUCAS-SOIL-2018.csv")
#df = df[(df["NUTS_0"]=="ES") & (df["NUTS_1"]=="ES4")&(df["NUTS_2"]=="ES41") & (df["NUTS_3"]=="ES418")]
#df = df[(df["NUTS_0"]=="FR") ]
lats = list(df["TH_LAT"])
longs = list(df["TH_LONG"])
print(len(lats))
coordinates = []

for i in range(len(lats)):
    coordinates.append((lats[i], longs[i]))


def get_pixel_value(tiff_file, coordinate):
    lat, lon = coordinate
    with rasterio.open(tiff_file) as src:
        row, col = src.index(lon, lat)
        pixel_value = src.read(1, window=((row, row + 1), (col, col + 1)))
        if pixel_value.shape[0] == 0 or pixel_value.shape[1] == 0:
            return None
    return pixel_value[0][0]


tiff_file_path = "fr_test.tiff"
i = 1
for coordinate in coordinates:
    pixel_value = get_pixel_value(tiff_file_path, coordinate)
    if pixel_value is not None:
        print(f"{i} Coordinate {coordinate}: Pixel Value = {pixel_value}")
        i = i + 1