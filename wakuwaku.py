import xml.etree.ElementTree as ET
from PIL import Image
from PIL import ImageDraw


tree = ET.parse('waku.xml')
root = tree.getroot()
def waku() :
    size = child.find("bndbox")
    size_min_width = int(size.find("xmin").text)
    size_min_height = int(size.find("ymin").text)
    size_max_width = int(size.find("xmax").text)
    size_max_height = int(size.find("ymax").text)
    size_start = (size_min_width, size_min_height)
    size_end = (size_max_width, size_max_height)
    print(size_start, size_end)
    draw = ImageDraw.Draw(img)
    color = "red"
    width = 2
    draw.rectangle([size_start, size_end], outline=color, width=width)

path_check = False
for child in root:
    if child.tag == "path":
        path_check = True
        img_text = child.text
        img = Image.open(img_text)
    if ((path_check) and (child.tag == "object")):
        name = child.find("name").text
        if name == "kuma" :
            waku()
        if name == "inu" :
            waku()
img.show()
img.save('wakuwaku.jpg')
