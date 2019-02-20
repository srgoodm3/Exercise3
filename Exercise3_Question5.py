import arcpy
arcpy.env.overwriteOutput=True
workspace=r"D:\610\Exercise3\Question5.gdb"
featureList = ["CapitalCities","Landmarks","HistoricPlaces","StateNames","Nationalities","Rivers"]
arcpy.CreateFileGDB_management(r"D:\610\Exercise3","Question5.gdb")
for feature in featureList:
    if feature=="Rivers":
        arcpy.CreateFeatureclass_management(workspace,feature,"POLYLINE")
    elif feature=="StateNames" or "Nationalities":
        arcpy.CreateFeatureclass_management(workspace,feature)
    else:
        arcpy.CreateFeatureclass_management(workspace,feature,"POINT")
print("Complete")