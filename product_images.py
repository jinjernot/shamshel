# Imports
import os
import xml.etree.ElementTree as ET

# Route to grab the XML files in the same directory as the script
xml_files = [file for file in os.listdir() if file.endswith(".xml")]

# Image dimensions in pixels, adjust values as needed
image_width = 500
image_height = 500

# Loop through each XML file
for xml_file_name in xml_files:
    # Define the corresponding HTML file name based on the XML file name
    html_file_name = os.path.splitext(xml_file_name)[0] + ".html"

    # Try to parse the XML file and get the root element
    try:
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

    # If an error occurs, print an error message and skip to the next file
    except ET.ParseError:
        print(f"Error parsing the XML file '{xml_file_name}'. Skipping.")
        continue

    # Create an empty list
    image_data = []

    # Loop through all 'image' elements in the XML file
    for asset_element in root.findall(".//image"):
        asset_embed_code_element = asset_element.find("image_url_https")
        asset_id_element = asset_element.find("file_name")

        # Check if the 'image_url_https' element is present
        if asset_embed_code_element is not None:
            image_url = asset_embed_code_element.text.strip()

            # If the URL is not empty, get the asset ID and add the data to the list
            if image_url:
                asset_id = asset_id_element.text.strip() if asset_id_element is not None else ""
                image_data.append({"url": image_url, "image_url_https": asset_id})

    # Create and write the HTML file with the collected image data
    with open(html_file_name, 'w') as html_file:
        html_file.write("<html>\n")
        html_file.write("<body>\n")

        # Loop through the collected image data and write HTML tags for each image
        for data in image_data:
            html_file.write(f"<p>URL: {data['url']}</p>\n")
            html_file.write(f"<img src={data['url']} alt='Image' width='{image_width}' height='{image_height}'>\n")

        html_file.write("</body>\n")
        html_file.write("</html>\n")

    # Print a message indicating that the HTML file was created and the number of resized image links
    print(f"HTML file '{html_file_name}' created with {len(image_data)} resized image links.")
