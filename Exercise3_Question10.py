import arcpy
arcpy.env.workspace="D:\610\Exercise3\Exercise 3.gdb"
arcpy.env.overwriteOutput=True
arcpy.SpatialJoin_analysis(r"D:\610\Exercise3\Exercise 3.gdb\Tracts",r"D:\610\Exercise3\Exercise 3.gdb\General_Offense",r"D:\610\Exercise3\Exercise 3.gdb\Tracts_GenOff_Join","","","","CONTAINS")
print("Complete")