import pandas as pd
import rasterio as rio
import os
import numpy as np

SCENE_PATH = "scenes"
CSVS_PATH = "csvs"
LUCAS_PATH = "LUCAS-SOIL-2018.csv"
BANDS = ["B01",
         "B02",
         "B03",
         "B04",
         "B05",
         "B06",
         "B07",
         "B08A",
         "B08",
         "B09",
         "B11",
         "B12",
         "EVI",
         "NDVI",
         "Agriculture"
         ]


def merge_scene(scene):
    pass


def find_tiff(tiffs, band):
    for tiff in tiffs:
        if band in tiff:
            return tiff
    return None


def get_coordinates():
    df = pd.read_csv(LUCAS_PATH)
    lats = list(df["TH_LAT"])
    longs = list(df["TH_LONG"])
    coordinates = []
    for i in range(len(lats)):
        coordinates.append((lats[i], longs[i]))
    return coordinates


def get_band_values(scene, band):
    the_scene_path = os.path.join(SCENE_PATH, scene)
    tiffs = os.listdir(the_scene_path)
    tiff = find_tiff(tiffs, band)
    tiff_path = os.path.join(tiff)
    coordinates = get_coordinates()
    pixels = []
    with rio.open(tiff_path) as src:
        for lat, lon in coordinates:
            row, col = src.index(lon, lat)
            pixel_value = src.read(1, window=((row, row + 1), (col, col + 1)))
            if pixel_value.shape[0] != 0 and pixel_value.shape[1] != 0:
                pixels.append([lat, lon, pixel_value[0][0]])
    return pixels


def process_scene(scene):
    df = pd.read_csv(LUCAS_PATH)
    for band in BANDS:
        pixels = get_band_values(scene, band)




    if not os.path.exists(CSVS_PATH):
        os.mkdir(CSVS_PATH)
    this_csv_path = os.path.join(CSVS_PATH, f"{scene}.csv")


def process_all_scenes():
    for scene in os.listdir(SCENE_PATH):
        process_scene(scene)
        merge_scene(scene)


if __name__ == "__main__":
    process_all_scenes()