import rasterio
import numpy as np

tiff_path = r"fr_test.tiff"

with rasterio.open(tiff_path) as src:
    raster_array = src.read(1)

print(np.min(raster_array))
print(np.mean(raster_array))
print(np.max(raster_array))