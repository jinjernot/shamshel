import os
import xml.etree.ElementTree as ET
import pandas as pd

xml_files = [file for file in os.listdir() if file.endswith(".xml")]

for xml_file_name in xml_files:
    # Create empty DataFrames for each category
    df_tech_specs = pd.DataFrame(columns=['Tag', 'Content'])
    df_features = pd.DataFrame(columns=['Tag', 'Content'])
    df_images = pd.DataFrame(columns=['Tag', 'Content'])

    try:
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        # Find all tech_specs, features, and images nodes
        tech_specs_list = root.findall(".//tech_specs")
        features_list = root.findall(".//features")
        images_list = root.findall(".//images")

        # Function to traverse XML tree and populate DataFrame
        def traverse(element, prefix="", df=None):
            for child in element:
                if len(child) > 0:
                    traverse(child, prefix + child.tag + '/', df)
                if child.text:
                    df.loc[len(df)] = [prefix + child.tag, child.text]

        # Iterate through tech_specs nodes and their children
        for tech_specs in tech_specs_list:
            traverse(tech_specs, df=df_tech_specs)

        # Iterate through features nodes and their children
        for features in features_list:
            traverse(features, df=df_features)

        # Iterate through images nodes and extract image_url_https from the image node
        for images in images_list:
            for image in images.findall('./image'):
                image_url_https = image.find('./image_url_https')
                if image_url_https is not None and image_url_https.text:
                    df_images.loc[len(df_images)] = ['images/image/image_url_https', image_url_https.text]

    except ET.ParseError:
        print(f"Error parsing the XML file '{xml_file_name}'. Skipping.")
        continue

    # Drop rows with NaN values in the 'Content' column
    df_tech_specs = df_tech_specs.dropna(subset=['Content'])
    df_features = df_features.dropna(subset=['Content'])
    df_images = df_images.dropna(subset=['Content'])

    # Save DataFrames to different sheets within the same Excel file
    excel_file_name = os.path.splitext(xml_file_name)[0] + ".xlsx"
    with pd.ExcelWriter(excel_file_name, engine='xlsxwriter') as writer:
        df_tech_specs.to_excel(writer, sheet_name='tech_specs', index=False)
        df_features.to_excel(writer, sheet_name='features', index=False)
        df_images.to_excel(writer, sheet_name='images', index=False)

    # Print confirmation
    print(f'DataFrames saved to {excel_file_name}')
