import xml.etree.cElementTree as ET
import pandas
import os

def build_file(dump1):
    data = ET.Element("dump")
    for i in dump1.processes:
        Node=ET.SubElement(data, 'Proc', name=i.name,pid=i.pid,memory_used_by_modules=str(i.memory_used_by_modules),memory_used_by_pages=str(i.memory_used_by_pages),memory_usability_percentage=str(i.memory_used_by_modules*100/i.memory_used_by_pages))
        for j in i.modules:
            Child=ET.SubElement(Node, 'Mod', name=j.name,base =  j.base,size=j.size)
            for k in j.pages:
                Kid=ET.SubElement(Child, 'PG',Asci=str(k.print_Ascci),NAsci=str(k.non_print_Ascci),Num=str(k.print_Ascci_Num),Ent=str(k.entropy),Size=str(k.size))
                #print("Child, 'PG', Asci={0} ,NAsci={1} , Num={2} , Ent={3}".format(k.print_Ascci,k.non_print_Ascci,k.print_Ascci_Num,int(k.entropy)))
                Kid.text = k.address
                #round
    tree = ET.ElementTree(data)
    #to remove threading uncomment the line below and comment the one below it
    tree.write("testxml.xml")
    
def combine_xml(files):
    first = None
    for filename in files:
        data = ET.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
    if first is not None:
        tree = ET.ElementTree(first)
        tree.write("testxml.xml")
      