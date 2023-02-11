import xml.etree.ElementTree as ET
from lxml import etree
import requests

def fromFile():

    parser = etree.XMLParser(recover=True)
    tree = ET.parse('./XML/test.xml', parser)
    root = tree.getroot()
    searchTags(root)

def fromURL():
    #testURL https://cap.corp.hp.com/capui/productFileOpen.action?path=/var/opt/cap-out/xmlfiles/fullload/ww-en/021015xxxxxx/021015649xxx/2101564959.xml
    url= input("pega la URL del CAP file: ")
    response = requests.get(url, verify=False)
    xml_content = response.content
    root = ET.fromstring(xml_content)
    searchTags(root)

def searchTags(root):
    tags = [elem.tag for elem in root.iter()]
    mandatory_tags = ["verga","osinstalled", "ioports", "processor", "chipset","image"]
    missing_elements = []
    for i in mandatory_tags:
        if i not in tags:
            missing_elements.append(i)

    print(missing_elements)

def main():
    print("Bienvenido a Predator-Mutator")
    user_input = input("1 para file, 2 para URL ")
    x = int(user_input)

    if x == 1:
        print("elegiste 1, leyendo el xml local...")
        fromFile()
    elif x == 2:
        print("elegiste 2, leyendo el xml desde URL...")
        fromURL()

if __name__ == "__main__":
    main()