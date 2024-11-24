import os
import pandas as pd

csv_file = '/home/daniel/Git/Israel-GeoInsights/scripts/iso-3166-folders/iso3166-alpha2.csv' 
countries_df = pd.read_csv(csv_file)

country_codes = countries_df['alpha-2'].dropna()

output_folder = '/home/daniel/Git/Israel-GeoInsights/Resources/iso-3166-folders'  
os.makedirs(output_folder, exist_ok=True)

# Create a folder for each country's alpha-2 code
for code in country_codes:
    folder_path = os.path.join(output_folder, code)
    os.makedirs(folder_path, exist_ok=True)

print(f"Folders created successfully in '{output_folder}'!")