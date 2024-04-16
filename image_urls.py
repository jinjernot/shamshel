import os
import xml.etree.ElementTree as ET
import pandas as pd
import requests

# Route to grab the XML files in the same directory as the script
xml_files = [file for file in os.listdir() if file.endswith(".xml")]

# Create an empty list to store unique image URLs and their response status
unique_image_data = []

# Image dimensions in pixels, adjust values as needed
image_width = 500
image_height = 500

# Loop through each XML file
for xml_file_name in xml_files:
    # Try to parse the XML file and get the root element
    try:
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

    # If an error occurs, print an error message and skip to the next file
    except ET.ParseError:
        print(f"Error parsing the XML file '{xml_file_name}'. Skipping.")
        continue

    # Loop through all 'image' elements in the XML file
    for asset_element in root.findall(".//image"):
        asset_embed_code_element = asset_element.find("image_url_https")

        # Check if the 'image_url_https' element is present
        if asset_embed_code_element is not None:
            image_url = asset_embed_code_element.text.strip()

            # If the URL is not empty and not already in the list, add it to the list
            if image_url:
                response = requests.head(image_url)
                status_code = response.status_code
                unique_image_data.append({"url": image_url, "status": status_code})

# Convert the list of unique image data to a pandas DataFrame
df = pd.DataFrame(unique_image_data)

# Save the DataFrame to an Excel file
excel_file_name = "image_urls.xlsx"
df.to_excel(excel_file_name, index=False)

# Print a message indicating that the Excel file was created and the number of unique URLs saved
print(f"Excel file '{excel_file_name}' created with {len(df)} unique image URLs with status.")
