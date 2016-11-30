#adapted from http://svn.osgeo.org/gdal/trunk/autotest/alg/rasterize.py

import os
import sys
from osgeo import gdal, ogr, osr

sr_wkt = 'LOCAL_CS["arbitrary"]'
sr = osr.SpatialReference( sr_wkt )

geotiff_filename = "treasure_island.tif"
ds = gdal.Open(geotiff_filename, gdal.GA_Update)

sr_wkt = 'LOCAL_CS["arbitrary"]'
sr = osr.SpatialReference( sr_wkt )

ds.SetProjection( sr_wkt )
rast_ogr_ds = ogr.GetDriverByName('Memory').CreateDataSource( 'wrk' )
rast_mem_lyr = rast_ogr_ds.CreateLayer( 'poly', srs=sr )

# Add a polygon.

wkt_geom_new = 'POLYGON((372 405, 176 90, 500 90, 372 405))'

feat = ogr.Feature( rast_mem_lyr.GetLayerDefn() )
feat.SetGeometryDirectly( ogr.Geometry(wkt = wkt_geom_new) )

rast_mem_lyr.CreateFeature( feat )

# Add a linestring.

wkt_geom = 'LINESTRING(1000 1000, 1100 1050)'

feat = ogr.Feature( rast_mem_lyr.GetLayerDefn() )
feat.SetGeometryDirectly( ogr.Geometry(wkt = wkt_geom) )

rast_mem_lyr.CreateFeature( feat )

# Run the algorithm.

ret = gdal.RasterizeLayer( ds, [3,2,1], rast_mem_lyr,
                       burn_values = [200,220,240] )


if ret != 1:
    print 'fail'
else:
    print 'success'
