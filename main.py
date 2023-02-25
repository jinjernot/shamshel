import xml.etree.ElementTree as ET
from lxml import etree
import glob
import pandas as pd
import os


def fromFile():
    """Read the XMLs from the folder"""
    parser = etree.XMLParser(recover=True)
    folder_path = "./XML/"
    csv_path = "./csv/"
    xml_files = glob.glob(folder_path + "*.xml")

    for xml_file in xml_files: #loop through all the files
        tree = ET.parse(xml_file, parser)
        root = tree.getroot()
        searchTags(root, csv_path, xml_file)

def searchTags(root, csv_path, xml_file):
    """Search for mandatory tags"""
    tags = [elem.tag for elem in root.iter()] #get all tags
    product_type = root.find("./hierarchy/product_type").attrib #look for product type to get the ID
    sku_number = root.find("./content/system/product_numbers/prodnum").text
    
    if product_type["pmoid"] == "12454": # Desktops & Workstations
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["osinstalled", "ioports", "processor", "chipset","image"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        DesktopDF = pd.DataFrame({"XML Missing": missing_elements})
        print(DesktopDF.to_string(index=False))
        csv_filename = os.path.splitext(xml_file)[0] + ".csv"
        DesktopDF.to_csv(os.path.join(csv_path, csv_filename), index=False)

    elif product_type["pmoid"] == "18972": # Printers
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["osinstalled", "ioports", "processor", "chipset","image"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        PrintDF = pd.DataFrame({"XML Missing": missing_elements})
        print(PrintDF.to_string(index=False))
        PrintDF.to_csv("./csv/print.csv", index=False)
        

    elif product_type["pmoid"] == "321957": # Laptops
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["batterylife","batteryrechrg","batterytype","batteryweightimp","batteryweightmet","cdromdvd","cloudserv","dispdescmetshort","dispdescshort","display","displaybright","displaycolorgamut","displaymet","displaysize","displaysizemet","ecohighlighgraphic","energyeffcomp","filter_processorspd","filter_storagetype","fingerprread","flashcache","flashcachenote","gcformfactor","gcnote","graphicseg_01card_01","graphicseg_01header","graphicseg_02card_01","graphicseg_02header","hd_01des","hd_02des","keybrd","maxbatterylifevideo","memlayout","memstdes_01","memstdnote","memstosimp","mousepntgdevice","osinstalled","osinstallednote","powersupplytype","processorcache","processorcoreinstalled","processorfamily","processorname","prodfinish","productcolour","storage_acceleration","swincluded","swpreinstalled","swprodfinance","webcam","wirelesstech"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        LaptopDF = pd.DataFrame({"XML Tags Missing": missing_elements})
        print(LaptopDF.to_string(index=False))
        LaptopDF.to_csv("./csv/laptop.csv", index=False)

def main():
    print("Bienvenido a Predator-Mutator")
    fromFile()

if __name__ == "__main__":
    main()
