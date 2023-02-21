import xml.etree.ElementTree as ET
from lxml import etree
import glob
import pandas as pd

def fromFile():
    parser = etree.XMLParser(recover=True)
    folder_path = "./XML/"
    xml_files = glob.glob(folder_path + "*.xml")

    for xml_file in xml_files:
        tree = ET.parse(xml_file, parser)
        root = tree.getroot()
        searchTags(root)

def searchTags(root):
    tags = [elem.tag for elem in root.iter()]
    product_type = root.find("./hierarchy/product_type").attrib
    sku_number = root.find("./content/system/product_numbers/prodnum").text
    
    if product_type["pmoid"] == "12454": # Desktops & Workstations
        print("Este SKU es de la jerarquia: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["osinstalled", "ioports", "processor", "chipset","image"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        df = pd.DataFrame({"XML Missing": missing_elements})
        print(df)

    elif product_type["pmoid"] == "18972": # Printers
        print("Este SKU es de la jerarquia: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["osinstalled", "ioports", "processor", "chipset","image"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        df = pd.DataFrame({"XML Missing": missing_elements})
        print(df)

    elif product_type["pmoid"] == "321957": # Laptops
        print("Este SKU es de la jerarquia: " + product_type["name"])
        print(sku_number + ":")
        mandatory_tags = ["batterylife","batteryrechrg","batterytype","batteryweightimp","batteryweightmet","cdromdvd","cloudserv","dispdescmetshort","dispdescshort","display","displaybright","displaycolorgamut","displaymet","displaysize","displaysizemet","ecohighlighgraphic","energyeffcomp","filter_processorspd","filter_storagetype","fingerprread","flashcache","flashcachenote","gcformfactor","gcnote","graphicseg_01card_01","graphicseg_01header","graphicseg_02card_01","graphicseg_02header","hd_01des","hd_02des","keybrd","maxbatterylifevideo","memlayout","memstdes_01","memstdnote","memstosimp","mousepntgdevice","osinstalled","osinstallednote","powersupplytype","processorcache","processorcoreinstalled","processorfamily","processorname","prodfinish","productcolour","storage_acceleration","swincluded","swpreinstalled","swprodfinance","webcam","wirelesstech"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        df = pd.DataFrame({"XML Missing": missing_elements})
        print(df)

def main():
    print("Bienvenido a Predator-Mutator")
    fromFile()

if __name__ == "__main__":
    main()
