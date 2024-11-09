import arcpy

input_raster = r'C:\Users\r\Desktop\idgp\idgp_label\processed_sichuan_land_cover_idgp.tif'

# 尝试重新构建属性表
arcpy.management.BuildRasterAttributeTable(input_raster, "Overwrite")

# 添加 Sym_Lab 字段（如果它还不存在）
field_name = "Sym_Lab"
if field_name not in [f.name for f in arcpy.ListFields(input_raster)]:
    arcpy.management.AddField(input_raster, field_name, "TEXT")

# 使用 UpdateCursor 更新字段
land_cover_map = {
    1: 'Evergreen_Needleleaf_Forests',
    2: 'Evergreen_Broadleaf_Forests',
    3: 'Deciduous_Needleleaf_Forests',
    4: 'Deciduous_Broadleaf_Forests',
    5: 'Mixed_Forests',
    6: 'Closed_Shrublands',
    7: 'Open_Shrublands',
    8: 'Woody_Savannas',
    9: 'Savannas',
    10: 'Grasslands',
    11: 'Permanent_Wetlands',
    12: 'Croplands',
    13: 'Urban_and_Built-up_Lands',
    14: 'Cropland_Natural_Vegetation_Mosaics',
    15: 'Permanent_Snow_and_Ice',
    16: 'Barren_or_Sparsely_Vegetated',
    17: 'Water_Bodies',
    255: 'Unclassified'
}

try:
    with arcpy.da.UpdateCursor(input_raster, ["Value", field_name]) as cursor:
        for row in cursor:
            value = row[0]
            # 为每个栅格值赋予标签
            row[1] = land_cover_map.get(value, "Unclassified")
            cursor.updateRow(row)
    print(f"Sym_Lab field updated for {input_raster}")

except Exception as e:
    print(f"Error processing {input_raster}: {e}")
