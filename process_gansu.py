import os
import arcpy

# 输入栅格路径
input_raster = r'C:\Path\To\Your\Raster.tif'

# IGBP分类字典
land_cover_map = {
    1: 'Evergreen Needleleaf Forests',
    2: 'Evergreen Broadleaf Forests',
    3: 'Deciduous Needleleaf Forests',
    4: 'Deciduous Broadleaf Forests',
    5: 'Mixed Forests',
    6: 'Closed Shrublands',
    7: 'Open Shrublands',
    8: 'Woody Savannas',
    9: 'Savannas',
    10: 'Grasslands',
    11: 'Permanent Wetlands',
    12: 'Croplands',
    13: 'Urban and Built-up Lands',
    14: 'Cropland/Natural Vegetation Mosaics',
    15: 'Permanent Snow and Ice',
    16: 'Barren or Sparsely Vegetated',
    17: 'Water Bodies',
    255: 'Unclassified'
}

# 确保栅格文件存在
if arcpy.Exists(input_raster):
    # 添加新的字段来存储符号化的标签
    arcpy.management.AddField(input_raster, "Symbology_Label", "TEXT")

    # 使用 UpdateCursor 更新栅格属性表
    with arcpy.da.UpdateCursor(input_raster, ["VALUE", "Symbology_Label"]) as cursor:
        for row in cursor:
            value = row[0]
            # 根据栅格值将标签应用到字段
            row[1] = land_cover_map.get(value, "Unclassified")  # 如果没有对应的值，默认标为 "Unclassified"
            cursor.updateRow(row)

    # 生成栅格属性表
    arcpy.management.BuildRasterAttributeTable(input_raster, "Overwrite")

    print("Symbology labels added and raster attribute table built.")

else:
    print(f"The raster file {input_raster} does not exist.")
