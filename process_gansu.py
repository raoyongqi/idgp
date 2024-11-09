import arcpy
import csv

# 输入栅格数据路径
raster = r"C:\path_to_your_raster\processed_land_cover.tif"

# 加载符号化表格（CSV文件）的路径
csv_file = r"C:\path_to_your_csv\land_cover_classification.csv"

# 读取CSV文件中的值和标签并存储为字典
value_label_map = {}
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过CSV表头
    for row in reader:
        value_label_map[int(row[0])] = row[1]

# 确保栅格图层存在，并准备进行符号化
if arcpy.Exists(raster):
    # 为栅格图层添加一个新的字段来存储符号化的标签
    arcpy.management.AddField(raster, "Symbology_Label", "TEXT")

    # 使用栅格数据并遍历每个像素值，给它们分配标签
    with arcpy.da.UpdateCursor(raster, ["VALUE", "Symbology_Label"]) as cursor:
        for row in cursor:
            value = row[0]
            # 根据栅格值将标签应用到字段
            row[1] = value_label_map.get(value, "Unclassified")  # 如果没有对应的值，默认标为"Unclassified"
            cursor.updateRow(row)

    # 现在可以使用这个字段进行符号化
    symbology_layer = arcpy.mapping.Layer(r"C:\path_to_your_style_file.lyr")  # 创建符号化图层

    # 应用符号化
    arcpy.management.ApplySymbologyFromLayer(raster, symbology_layer)
    print(f"Symbolization applied using {csv_file}.")

else:
    print(f"Raster {raster} does not exist.")