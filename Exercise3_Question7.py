import arcpy
arcpy.env.workspace = "D:\610\Exercise3\Exercise 3.gdb"
arcpy.env.overwriteOutput=True
workspace=r"D:\610\Exercise3\Exercise 3.gdb"
arcpy.MakeFeatureLayer_management(r"D:\610\Exercise3\Exercise 3.gdb\CallsforService","theft_lyr")
TheftCalls = arcpy.SelectLayerByAttribute_management("theft_lyr","NEW_SELECTION","CFSType = 'Theft Call'")
arcpy.CopyFeatures_management(TheftCalls,r"D:\610\Exercise3\Exercise 3.gdb\TheftCalls")
print("Complete")