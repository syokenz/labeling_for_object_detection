#
# for fn in `ls datasets/Annotations/`
# do
#   python hoge.py datasets/Annotations/$fn >> info.dat 2>> bg.txt
# done  
#
import xml.etree.ElementTree as ET
import sys

#XmlData = open("datasets/Annotations/img_00111.xml").read()
xmlpath = sys.argv[1]
imgpath = xmlpath.replace("xml","png").replace("Annotations","JPEGImages")
try:
    XmlData = open(xmlpath).read()
    root = ET.fromstring(XmlData)
    xmin = root.find(".//xmin").text
    ymin = root.find(".//ymin").text
    xmax = root.find(".//xmax").text
    ymax = root.find(".//ymax").text
    
    str = "{0} 1 {1} {2} {3} {4}".format(imgpath, xmin, ymin, int(xmax) - int(xmin), int(ymax) - int(ymin))
    
    print(str)
    
except :
    # There is no object
    sys.stderr.write(imgpath + "\n")
