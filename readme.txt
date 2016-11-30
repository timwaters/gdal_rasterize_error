for: http://lists.osgeo.org/pipermail/gdal-dev/2016-November/045622.html
[gdal-dev] Seg fault & error running gdal_rasterize on a non georeferenced raster

'm seeing an error running GDAL 1.11.3 on Ubuntu 16.04LTS and 2.10.
There was no error and it worked fine with GDAL 1.10.1 on Ubuntu
14.04LTS.

I see the error running gdal_rasterize utility and also in python.

gdal_rasterize -i  -burn 17 -b 1 -b 2 -b 3 clipping.gml -l features masked.tif

Python script for reference
https://gist.github.com/timwaters/a8da4e3e209aaae955d23446c3925125

ERROR 1: Unable to compute a transformation between pixel/line
and georeferenced coordinates for masked.tif
There is no affine transformation and no GCPs.
Segmentation fault (core dumped)

I have tried to assign the non georeferenced raster an SRS LOCAL_CS["arbitrary"]
gdal_translate -a_srs 'LOCAL_CS["arbitrary"]' masked.tif
masked_ref.tif but got the same error when rasterizing.

The use case is for mapwarper.net where people can upload images and
create clipping masks around the rectangular images (to remove borders
etc) before adding control points and geo referencing them. Ideally,
I'd like to be able to keep the clipping on the unwarped images as
it's easier for users e.g often just drawing a rectangle than doing it
on the warped ones with many vertices and having to re-do each time
the georeferencing is changed.

Is this a new bug? The changelog didn't show anything new or changed
for gdal_rasterize from what I could see but perhaps I'm missing
something obvious. Is there a workaround? Perhaps there's an
Imagemagick command that would do it?




gdalinfo treasure_island.tif
Driver: GTiff/GeoTIFF
Files: treasure_island.tif
Size is 540, 514
Coordinate System is `'
Image Structure Metadata:
  COMPRESSION=DEFLATE
  INTERLEAVE=PIXEL
Corner Coordinates:
Upper Left  (    0.0,    0.0)
Lower Left  (    0.0,  514.0)
Upper Right (  540.0,    0.0)
Lower Right (  540.0,  514.0)
Center      (  270.0,  257.0)
Band 1 Block=540x5 Type=Byte, ColorInterp=Red
  Overviews: 270x257, 135x129, 68x65, 34x33, 17x17, 9x9
Band 2 Block=540x5 Type=Byte, ColorInterp=Green
  Overviews: 270x257, 135x129, 68x65, 34x33, 17x17, 9x9
Band 3 Block=540x5 Type=Byte, ColorInterp=Blue
  Overviews: 270x257, 135x129, 68x65, 34x33, 17x17, 9x9


gdal_rasterize -i  -burn 17 -b 1 -b 2 -b 3 20.gml -l features treasure_island.tif
Warning : the output raster dataset has a SRS, but the input vector layer SRS is unknown.
Ensure input vector has the same SRS, otherwise results might be incorrect.
ERROR 1: Unable to compute a transformation between pixel/line
and georeferenced coordinates for treasure_island.tif.
There is no affine transformation and no GCPs.
0Segmentation fault (core dumped)



python ras.py 
ERROR 1: Unable to compute a transformation between pixel/line
and georeferenced coordinates for treasure_island.tif.
There is no affine transformation and no GCPs.
Segmentation fault (core dumped)
tim@capricorn:~/work/leiden/vagrant_gdal/
