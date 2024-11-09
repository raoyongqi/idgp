import os
import rasterio
import numpy as np

# Input and output folder paths
input_folder = 'idgp'  # Change to your input folder path
output_folder = 'idgp_label'  # Change to your output folder path

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Define the IGBP classification mapping dictionary (land cover types)
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

# Traverse all .tif files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.tif'):
        input_path = os.path.join(input_folder, filename)
        
        # Read the GeoTIFF file
        with rasterio.open(input_path) as src:
            land_cover_data = src.read(1)  # Read the first band (LC_Type1)

            # Replace numeric values with corresponding category names
            land_cover_classes = np.vectorize(lambda x: land_cover_map.get(x, 'Unclassified'))(land_cover_data)

            # Output file path
            output_path = os.path.join(output_folder, f'processed_{filename}')
            
            # Save the new GeoTIFF with the integer class values (not string) for proper GeoTIFF storage
            with rasterio.open(output_path, 'w', 
                               driver='GTiff',
                               count=1, dtype='int32',  # Use 'int32' for classification codes
                               height=land_cover_data.shape[0], 
                               width=land_cover_data.shape[1],
                               crs=src.crs, 
                               transform=src.transform) as dst:
                dst.write(land_cover_data.astype(np.int32), 1)  # Write integer class values to file

            print(f"Processed: {filename}")

print("All files processed.")
