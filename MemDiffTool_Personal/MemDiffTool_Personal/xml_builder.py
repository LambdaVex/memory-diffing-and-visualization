import xml.etree.cElementTree as ET
import pandas
import os

def build_file(dump1):
    data = ET.Element("dump")
    for i in dump1.processes:
        Node=ET.SubElement(data, 'Proc', name=i.name,pid=i.pid)
        for j in i.modules:
            Child=ET.SubElement(Node, 'Mod', name=j.name,base =  j.base,size=j.size )
            for k in j.pages:
                Kid=ET.SubElement(Child, 'PG')
                Kid.text = k.address
   
    tree = ET.ElementTree(data)
    tree.write("testxml.xml")