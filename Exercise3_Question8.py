import arcpy
arcpy.env.workspace="D:\610\Exercise3\Exercise 3.gdb"
arcpy.env.overwriteOutput = True
count=arcpy.GetCount_management(r"D:\610\Exercise3\Exercise 3.gdb\CallsforService")
print("There are " +str(count)+" records in the CallsforService feature class")
print("Complete")