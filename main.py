import xml.etree.ElementTree as ET
from lxml import etree
import glob
import pandas as pd
import os

def fromFile():
    """Read the XMLs from the folder"""
    parser = etree.XMLParser(recover=True)
    folder_path = "./XML/"
    csv_path = "./csv"
    xml_files = glob.glob(folder_path + "*.xml")
    mainDF= pd.DataFrame(columns=["XML Tags Missing"])
    mainDF.to_csv("chida.csv", index=False)

    for xml_file in xml_files: #loop through all the files
        tree = ET.parse(xml_file, parser)
        root = tree.getroot()
        searchTags(root, csv_path, xml_file,mainDF)
        imgs(root, csv_path, xml_file)
    
    dfs = []
    for filename in os.listdir(csv_path): #loop through all the csvs
        if filename.endswith('.csv'):
            filepath = os.path.join(csv_path, filename)
            df = pd.read_csv(filepath)
            dfs.append(df)
    concat_df = pd.concat(dfs, axis=1)
    concat_df.to_csv('missing_content.csv', index=False)

def searchTags(root, csv_path, xml_file,mainDF):
    """Search for mandatory tags"""
    tags = [elem.tag for elem in root.iter()] #get all tags
    product_type = root.find("./hierarchy/product_type").attrib #look for product type to get the ID
    sku_number = root.find("./content/system/product_numbers/prodnum").text
    
    if product_type["pmoid"] == "12454": # Desktops & Workstations
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["chassistype","marketing_tier","prodshortnamespecs","prodlongnamespecs","osinstalleddes01","osinstalled","chipset","processorfamily","processortype","processorname","memmax_01","memslots","memstdes_01","memstnote_01","memstosimp","hdcntrltype_01","hdcntrltype_01hdmin","hdcntrltype_01hdmax","hd_01des","filter_storagetype","expanslots","ioports_01_location","ioports","netinterface","managefeatures","swincluded","securitymgmt","weightmet","weightus","weightpackmet","weightpackus","dimenmet","dimenus","dimenpackmet","dimenpackus","powersupply","powersupplyfixed","upc","wrntyfeatures"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        DesktopDF = pd.DataFrame({"XML Missing": missing_elements})
        new_row = {'XML Tags Missing' : sku_number}
        DesktopDF.loc[-1] = new_row
        DesktopDF.index = DesktopDF.index + 1
        DesktopDF = DesktopDF.sort_index()

        csv_filename = os.path.splitext(xml_file)[0] + ".csv"
        csv_filename = csv_filename.replace("./XML/","")
        DesktopDF.to_csv(os.path.join(csv_path, csv_filename), index=False)

    elif product_type["pmoid"] == "18972": # Printers
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = [""]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        PrintDF = pd.DataFrame({"XML Missing": missing_elements})
        new_row = {'XML Tags Missing' : sku_number}
        PrintDF.loc[-1] = new_row
        PrintDF.index = PrintDF.index + 1
        PrintDF = PrintDF.sort_index()

        csv_filename = os.path.splitext(xml_file)[0] + ".csv"
        csv_filename = csv_filename.replace("./XML/","")
        PrintDF.to_csv(os.path.join(csv_path, csv_filename), index=False)

    elif product_type["pmoid"] == "321957": # Laptops
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["marketing_tier","graphicseg_01header","graphicseg_01card_01","productcolour","prodfinish","weightmet","weightmetnote","weightus","weightpackmet","weightpackus","dimenmet","dimenus","dimenpackmet","dimenpackus","batterytype","batterylife","batteryrechrg","batteryrechrgftntnbr","batterytypenote","powersupplytype","webcam","ioports","wirelesstech","wirelesstechnonote","displaysize","displaysizemet","display","displaymet","screenbodyratio","displaycolorgamut","displaybright","filter_storagetype","cloudserv","cloudservftntnbr","hd_01des","memstdes_01","memstdnote","keybrd","mousepntgdevice","audiofeat","chipset","processorname","processornameftntnbr","processorfamily","swincluded","swprodfinance","osinstalled"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        LaptopDF = pd.DataFrame({"XML Tags Missing": missing_elements})
        new_row = {'XML Tags Missing' : sku_number}
        LaptopDF.loc[-1] = new_row
        LaptopDF.index = LaptopDF.index + 1
        LaptopDF = LaptopDF.sort_index()
        print(LaptopDF)
        LaptopDF.to_csv("chida.csv", mode= "a", header=False, index=False)
        


      #  csv_filename = os.path.splitext(xml_file)[0] + ".csv"
       # csv_filename = csv_filename.replace("./XML/","")
      #  LaptopDF.to_csv(os.path.join(csv_path, csv_filename), index=False)

def imgs(root, csv_path, xml_file):
    print("Images")
    images = []

    for tag in root.findall('.//image'):
        values = []
        for child in tag:
            values.append(child.text)
        images.append(values)
    df = pd.DataFrame(images, columns=["index","dpi_resolution","image_url_http","pixel_width","content_type","color","full_title","action","document_type","pixel_height","master_object_name","file_name","document_type_detail","background","cmg_acronym","image_url_https","orientation",""], index=None)
    #delete_cols = ["index","dpi_resolution","image_url_http","pixel_width","content_type","color","full_title","action","document_type","pixel_height","master_object_name","file_name","document_type_detail","background","cmg_acronym"]
    #df = df.drop(columns=delete_cols)

    csv_filename = os.path.splitext(xml_file)[0] + ".csv"
    csv_filename = csv_filename.replace("./XML/","")
    df.to_csv(os.path.join(csv_path, csv_filename), index=False)

def main():
    print("Bienvenido a Predator-Mutator")
    fromFile()
    


if __name__ == "__main__":
    main()
