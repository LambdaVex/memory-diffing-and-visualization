from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.ElementTree as ET
import memory_dump as md
import process as pr
import module as mod
import page as pge
import time
import heatmap_processess as phmap

def prase():
    tree = ET.parse('testxml.xml')
    root = tree.getroot()


    #print(root[1][0][1].text)
    #print(root[1][0].attrib['size'])
    print(len(root[1][0]))

    start_time = time.time()
    heatmap_dump=md.MemoryDump("heatmap")

    for i in range(0,len(root)):
        #print("{0}:{1}".format(root[i].attrib['name'],root[i].attrib['pid']))
        process=pr.Process(root[i].attrib['name'],root[i].attrib['pid'])
        heatmap_dump.processes.append(process)
        for j in range(0,len(root[i])):
            #print("--------{0}:{1}".format(root[i][j].attrib['name'],root[i][j].attrib['base']))
            module=mod.Module(root[i][j].attrib['name'],root[i][j].attrib['base'],root[i][j].attrib['size'])
            heatmap_dump.processes[i].modules.append(module)
            for k in range(0,len(root[i][j])):
                #print("----------------{0}".format(root[i][j][k].text))
                tpage=pge.Page(root[i][j][k].text,'1','1','1')
                heatmap_dump.processes[i].modules[j].pages.append(tpage)

    for i in heatmap_dump.processes:
        for j in i.modules:
            Val_New=[]
            if(len(j.pages)>0):
                for k in range(len(j.pages)):
                    if(k+1!=len(j.pages)):
                        Val_New.append(j.pages[k])
                        distance=(int((int(j.pages[k+1].address,16)-int(j.pages[k].address,16))/4096))
                        Val_New=Val_New+[pge.Page("-1","-1","-1","-1")]*((int(distance))-1)
                Val_New.append(j.pages[len(j.pages)-1])
                j.hmpages=Val_New


    #calc max
    '''
    list=[]
    for i in heatmap_dump.processes:
        for j in i.modules:
            print("{0} - {1} - {2}".format(i.pid,j.name,len(j.hmpages)))
            list.append(len(j.hmpages))
    print(max(list))
    '''

    #5152
    ''' 
    Sum=0
    for i in heatmap_dump.processes:
        #print("Process: "+str(i.pid)+" has "+str(len(i.modules))+" Modules")
        Sum+=len(i.modules)
    print(Sum)
    #print(len(heatmap_dump.processes[3].modules))
    '''
    '''
    for i in heatmap_dump.processes[1].modules[1].hmpages:
        print(i.address+" ", end="")
    '''
    phmap.display_processheatmap(heatmap_dump)
    #print(heatmap_dump.processes[1].modules[0].hmpages)
    #print(len(heatmap_dump.processes[len(heatmap_dump.processes)-1].modules[len(heatmap_dump.processes[len(heatmap_dump.processes)-1].modules)-1].hmpages))
    #print(max(list))
    print("--- %s seconds ---" % (time.time() - start_time))



    #T=root[0].attrib['pid']
    #print(T)




    #Attrib
    '''
    In [52]: import xml.etree.ElementTree as ET

    In [53]: xml=ET.fromstring(contents)

    In [54]: xml.find('./bar').attrib['key']
    Out[54]: 'value'

    ====================> T=root[0].attrib['pid']
    '''
