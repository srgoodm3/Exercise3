import arcpy
arcpy.env.workspace = "D:\610\Exercise3\Exercise 3.gdb"
arcpy.env.overwriteOutput = True
feature=r"D:\610\Exercise3\Exercise 3.gdb\CallsforService"
arcpy.AddField_management(feature,"Crime_Explanation","TEXT")
fields=["CFSType","Crime_Explanation"]
with arcpy.da.UpdateCursor(feature,fields) as cursor:
    for row in cursor:
        if row[0]=="Burglary Call":
            row[1]="This is a burglary"
        cursor.updateRow(row)
    del cursor
print("Complete")