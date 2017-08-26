# -*- coding: utf-8 -*-
#
# SSD向けに作った学習データ(XML)をOpenCVのカスケード分析ように変換する
# 使い方
#
# for fn in `ls datasets/Annotations/`
# do
#   python trans_to_cascade_train_model.py datasets/Annotations/$fn >> info.dat 2>> bg.txt
# done  
#
# http://shkh.hatenablog.com/entry/2012/11/03/052251
#
import xml.etree.ElementTree as ET
import sys

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
