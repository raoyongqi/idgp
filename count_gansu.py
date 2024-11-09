import arcpy

# 输入栅格文件路径
input_raster = r'C:\Users\r\Desktop\idgp\idgp_label\processed_gansu_idgp_2020.tif'

# 获取栅格的属性表
fields = arcpy.ListFields(input_raster)
print(fields)
count_field = "Count"  # 属性表中像素计数字段名称
value_field = "SymLab"  # 栅格值字段名

# 获取栅格值及其对应的像素计数
cursor = arcpy.da.SearchCursor(input_raster, [value_field, count_field])

# 生成一个字典，按计数值排序
value_count = {}

# 填充字典并过滤掉 'Unclassified' 栅格值
for row in cursor:
    value = row[0]
    if value != "Unclassified":  # 过滤掉 'Unclassified' 栅格值
        value_count[value] = row[1]

# 排序并获取前5个值
sorted_values = sorted(value_count.items(), key=lambda x: x[1], reverse=True)
top_5_values = [item[0] for item in sorted_values[:5]]

print("Top 5 values based on pixel count (excluding 'Unclassified'):", top_5_values)
