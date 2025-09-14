#import gdal
from osgeo import gdal
import geopandas, rasterio, pandas, numpy, matplotlib
print("All packages imported successfully!")
print(f"GDAL version: {gdal.__version__}")
print(f"GeoPandas version: {geopandas.__version__}")