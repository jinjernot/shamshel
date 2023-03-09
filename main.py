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
    mainDF = pd.DataFrame(columns=["ando viendo como quitar este columna lol"])
    mainDF.to_csv("chida.csv", index=False)

    for xml_file in xml_files: #loop through all the files
        tree = ET.parse(xml_file, parser)
        root = tree.getroot()
        searchTags(root)
        imgs(root)


def searchTags(root):
    """Search for mandatory tags"""
    tags = [elem.tag for elem in root.iter()] #get all tags
    product_type = root.find("./hierarchy/product_type").attrib #look for product type to get the ID
    sku_number = root.find("./content/system/product_numbers/prodnum").text
    
    if product_type["pmoid"] == "12454": # Desktops & Workstations
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number)
        mandatory_tags = ["chassistype","marketing_tier","prodshortnamespecs","prodlongnamespecs","osinstalleddes01","osinstalled","chipset","processorfamily","processortype","processorname","memmax_01","memslots","memstdes_01","memstnote_01","memstosimp","hdcntrltype_01","hdcntrltype_01hdmin","hdcntrltype_01hdmax","hd_01des","filter_storagetype","expanslots","ioports_01_location","ioports","netinterface","managefeatures","swincluded","securitymgmt","weightmet","weightus","weightpackmet","weightpackus","dimenmet","dimenus","dimenpackmet","dimenpackus","powersupply","powersupplyfixed","upc","wrntyfeatures"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        DesktopDF = pd.DataFrame({"XML Tags Missing": missing_elements})
        new_row = {'XML Tags Missing' : sku_number}
        DesktopDF.loc[-1] = new_row
        DesktopDF.index = DesktopDF.index + 1
        DesktopDF = DesktopDF.sort_index()
        mainDF = pd.read_csv("chida.csv")
        updated_df= pd.concat([mainDF, DesktopDF], axis=1)
        updated_df.to_csv('chida.csv', index=False)


    elif product_type["pmoid"] == "18972": # Printers
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number)
        mandatory_tags = ["codename","prodnameshort","blueangelcompli","electromagcompat","energyeffcomp","energystar","safety","inboxcable","whatsinbox","dimenmet","dimenmetmax","dimenpackmet","dimenpackus","dimen","dimenus","dimenusmax","weightmet","weightpackmet","weightpackus","weightus","saservices","wrntyfeatures","prntadvfeat","powerconsump","powersupply","powersupplytype","connectstd","jdnetsuppted","networkcap","wirelesscap","cpynumber","cpyredenlarge","cpyresblk","cpyresclr","cpyspdnorblka4","cpyspdnorblkus","cpyspdnorclra4","cpyspdnorclrus","dgfeaturesstand","display","accoustemisspow","accoustemisspressbyrdy","humidityop","humidityoprec","tempopcent","tempopfar","tempopreccent","tempoprecfar","tempstrgcent","tempstrgfar","faxcolor","faxspd","faxspda4","memmax","memstd","memupgrade","prntresclrbest","prnttechres","prntspdblknor","prntspdblknora4","prntspdclrnor","prntspdclrnora4","firstpagea4ready","firstpageclra4ready","firstpageclrready","firstpageready","aiofunctions","duplexprnt","dutycycle","dutycyclea4","dutycycleavgprntvol","hdcapprntr","papertrystd","prntlangstd","prntmgmt","prnttech","typeface","inputcapmaxenv","inputcapstd","mediatypecaptray1","outputcapstd","paperhandleinputstd","paperhandleoutputstd","processorspd","numofsimusers","typenergycompnum","scanresenh","scanreshw","scanresopt","bitdepth","scanadf","scanclr","scanformat","scangrayscale","scaninput","scansizemaxadfmet","scansizemaxadfus","scansizemaxmet","scansizemaxus","scansizeminadfmet","scansizeminadfus","scantwainver","scantype","securitymgmt","maccompat","swincluded","suppliescartridge","mediasizeadf","mediasizecustmet","mediasizecustus","mediasizestdmet","mediasizestdus","mediasizetray1","mediatype","mediaweightadf","mediaweightadfus","mediaweightmet","mediaweighttray1","mediaweightus","cntrlpanel","sysreqminmac","sysreqsmin","environspec","airprintcap","scanspdnora4","ordsupplies","suppliescartridgeftntnbr","topfeatureslist","usersandprintvol","keymediasizestdus","keymediasizestdmet","specialfeature","printspeed"]
        missing_elements = []
        for i in mandatory_tags:
            if i not in tags:
                missing_elements.append(i)
        PrintDF = pd.DataFrame({"XML Tags Missing": missing_elements})
        new_row = {'XML Tags Missing' : sku_number}
        PrintDF.loc[-1] = new_row
        PrintDF.index = PrintDF.index + 1
        PrintDF = PrintDF.sort_index()
        mainDF = pd.read_csv("chida.csv")
        updated_df= pd.concat([mainDF, PrintDF], axis=1)
        updated_df.to_csv('chida.csv', index=False)

    elif product_type["pmoid"] == "321957": # Laptops
        print("This SKU is from Hierarchy: " + product_type["name"])
        print(sku_number)
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
        mainDF = pd.read_csv("chida.csv")
        updated_df= pd.concat([mainDF, LaptopDF], axis=1)
        updated_df.to_csv('chida.csv', index=False)

def imgs(root):

    print("Images")
    images = []

    for tag in root.findall('.//image'):
        values = []
        for child in tag:
            values.append(child.text)
        images.append(values)
    imageDF = pd.DataFrame(images, columns=["ranking","dpi_resolution","image_url_http","pixel_width","content_type","color","full_title","action","document_type","pixel_height","master_object_name","file_name","document_type_detail","background","cmg_acronym","image_url_https","orientation","asd"])
    #delete_cols = ["index","dpi_resolution","image_url_http","pixel_width","content_type","color","full_title","action","document_type","pixel_height","master_object_name","file_name","document_type_detail","background","cmg_acronym"]
    #df = df.drop(columns=delete_cols)
    print(imageDF)

    #writer = pd.ExcelWriter("final.xlsx", engine="xlsxwriter",)
    imageDF.to_csv("oli.csv", index=False)

def main():
    print("Bienvenido a Predator-Mutator")
    fromFile()

if __name__ == "__main__":
    main()
