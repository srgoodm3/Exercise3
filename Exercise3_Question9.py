import arcpy
arcpy.env.workspace="D:\610\Exercise3\Question5.gdb"
arcpy.env.overwriteOutput = True
workspace=r"D:\610\Exercise3\Question5.gdb"
feature=arcpy.CreateFeatureclass_management(workspace,"Exercise3")
arcpy.AddField_management(feature,"Stuff","TEXT")
arcpy.CreateDomain_management(workspace,"StuffDomain","","SHORT","CODED")
arcpy.AssignDomainToField_management(feature,"Stuff","StuffDomain")
count=0
while count<5:
    arcpy.AddCodedValueToDomain_management(workspace,"StuffDomain",count,count)
    count+=1
print("Complete")