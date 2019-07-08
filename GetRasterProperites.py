# Matt Crichton
# 3/1/18
# Creating a function to extract properties of a raster. This code can be imported to ArcGIS
# as a custom tool.

import arcpy
# Create empty dictionary to put props in below
raster_props = {}

# Defining a function
def get_raster_props(in_raster):
    # Creating a variable to store the input rasters
    r = arcpy.Raster(in_raster)
    # "x_center" is a key in the dictionary. This key stores the data in that postition
    raster_props["x_center"] = r.extent.XMin + (r.extent.XMax - r.extent.XMin)
    raster_props["y_center"] = r.extent.YMin + (r.extent.YMax - r.extent.YMin)
    raster_props["max_elev"] = r.maximum
    raster_props["min_elev"] = r.minimum
    raster_props["no_data"] = r.noDataValue
    raster_props["terr_width"] = r.width
    raster_props["terr_height"] = r.height
    raster_props["terr_call_res"] = r.meanCellHeight

# Create a raster object equal to the input raster
input_raster = arcpy.GetParameterAsText(0)
get_raster_props(input_raster)

# Since each key is a double, we must cast it as a string to concatenate each value to the output message.
arcpy.AddMessage("x_center " + str(raster_props["x_center"]))
arcpy.AddMessage("y_center " + str(raster_props["y_center"]))
arcpy.AddMessage("max_elev " + str(raster_props["max_elev"]))
arcpy.AddMessage("min_elev " + str(raster_props["min_elev"]))
arcpy.AddMessage("no_data " + str(raster_props["no_data"]))
arcpy.AddMessage("terr_width " + str(raster_props["terr_width"]))
arcpy.AddMessage("terr_height " + str(raster_props["terr_height"]))
arcpy.AddMessage("terr_call_res " + str(raster_props["terr_call_res"]))
