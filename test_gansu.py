import arcpy

# 输入栅格文件路径
input_raster = r'C:\Users\r\Desktop\idgp\idgp_label\processed_gansu_idgp_2020.tif'

# 获取栅格文件的所有字段
fields = arcpy.ListFields(input_raster)

# 遍历字段并打印字段名称
for field in fields:
    print(f"Field name: {field.name}")
