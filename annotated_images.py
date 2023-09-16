import os
import xml.etree.ElementTree as ET


xml_files = [file for file in os.listdir() if file.endswith(".xml")]
image_width = 300
image_height = 300

for xml_file_name in xml_files:
    # Define the HTML file name based on the XML file name
    html_file_name = os.path.splitext(xml_file_name)[0] + ".html"

    try:
        tree = ET.parse(xml_file_name)
        root = tree.getroot()
    except ET.ParseError:
        print(f"Error parsing the XML file '{xml_file_name}'. Skipping.")
        continue

    image_data = []

    for asset_element in root.findall(".//asset"):
        asset_embed_code_element = asset_element.find("asset_embed_code")
        asset_id_element = asset_element.find("asset_id")
        if asset_embed_code_element is not None:
            image_url = asset_embed_code_element.text.strip()
            if image_url:
                asset_id = asset_id_element.text.strip() if asset_id_element is not None else ""
                image_data.append({"url": image_url, "asset_id": asset_id})

    with open(html_file_name, 'w') as html_file:
        html_file.write("<html>\n")
        html_file.write("<body>\n")

        for data in image_data:
            html_file.write(f"<p>Asset ID: {data['asset_id']}</p>\n")
            html_file.write(f"<img src={data['url']}' alt='Image' width='{image_width}' height='{image_height}'>\n")

        html_file.write("</body>\n")
        html_file.write("</html>\n")

    print(f"HTML file '{html_file_name}' created with {len(image_data)} resized image links.")
