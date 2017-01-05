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
                Kid=ET.SubElement(Child, 'PG',Asci=str(k.print_Ascci),NAsci=str(k.non_print_Ascci),Num=str(k.print_Ascci_Num),Ent=str(round(k.entropy)))
                #print("Child, 'PG', Asci={0} ,NAsci={1} , Num={2} , Ent={3}".format(k.print_Ascci,k.non_print_Ascci,k.print_Ascci_Num,int(k.entropy)))
                Kid.text = k.address
                #round
    tree = ET.ElementTree(data)
    #remove the dump.start when removing threading and write only tree.write(name)
    tree.write("testxml_withthread_number_"+dump1.start+".xml")