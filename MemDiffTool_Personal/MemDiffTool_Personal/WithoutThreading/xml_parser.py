from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from math import pi
from bokeh.io import output_file, show, vplot
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.plotting import figure
import xml.etree.ElementTree as ET
import memory_dump as md
import process as pr
import module as mod
import page as pge
import time
import heatmap_processess as phmap
import pandas as pd
import numpy as NP
import bokeh.palettes as bp
import configuration as co
import heatmap_processess as phmap
import heatmap_MemoryDump as memmap
import math
import pandas
import bisect_module as bi
import heatmap_summary as shmap
import toolz as tz

def get_index(list_modules,module):
    for index, item in enumerate(list_modules):
        if item.name == module:
            break
        else:
            index = -1
    return index
def parse(heatmap_dump,filename):

    #start_time = time.time()
    

    #tree = ET.parse('testxml.xml')
    tree = ET.parse(filename)
    root = tree.getroot()

    #print(root[1][0][1].text)
    #print(root[1][0].attrib['size'])
    #print(len(root[1][0]))

    for i in range(0,len(root)):
        #print("{0}:{1}".format(root[i].attrib['name'],root[i].attrib['pid']))
        process=pr.Process(root[i].attrib['name'],root[i].attrib['pid'])
        #print("add process: "+process.name)
        heatmap_dump.processes.append(process)
        for j in range(0,len(root[i])):
            #print("--------{0}:{1}".format(root[i][j].attrib['name'],root[i][j].attrib['base']))
            module=mod.Module(root[i][j].attrib['name'],root[i][j].attrib['base'],root[i][j].attrib['size'])
            heatmap_dump.processes[i].modules.append(module)
            for k in range(0,len(root[i][j])):
                #print("----------------{0}".format(root[i][j][k].text))
                tpage=pge.Page(root[i][j][k].text,root[i][j][k].attrib['Asci'],root[i][j][k].attrib['NAsci'],root[i][j][k].attrib['Num'],root[i][j][k].attrib['Ent'],root[i][j][k].attrib['Size'])
                
                heatmap_dump.processes[i].modules[j].pages.append(tpage)
    return heatmap_dump
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])     
 

if __name__ == '__main__':
   #print("ENTER")
    #heatmap_dump=prase()

    heatmap_dump=md.MemoryDump("heatmap")

    #filename_1="Complete_XML.xml"
    filename_1="Resources/MemDump.xml"
    #filename_2="testxml_withthread_number_14.xml"
    #filename_3="testxml_withthread_number_27.xml"
   
    heatmap_dump=parse(heatmap_dump,filename_1)

    list_modules=[]
    

   
    #Omit the first one
    for pr in heatmap_dump.processes:
        for mod in range(1,len(pr.modules)):
            list_modules.append(pr.modules[mod])
    
 
    list_modules.sort(key = lambda x: x.base)
    list_modules=list(tz.unique(list_modules, key=lambda x: x.name))


    # THIS IS THE FIRST WAY TO DO IT, REMEMBER BY DECLARING EVERY MODULE FOR EVERY PROCESS 
    '''
    for pr in heatmap_dump.processes:
        pr.summodules=[0]*len(list_modules)
        #print(len(list_modules))
        counter=0
        for mod in pr.modules:
           #print(mod.name)
           index=get_index(list_modules,mod.name)
           if(index!=-1):
               counter=counter+1
               pr.summodules[index]=1
        #print(pr.summodules)
        pr.summodules=[x * ((counter/len(list_modules))*1000) for x in pr.summodules]
        #print(pr.summodules)
        #time.sleep(5)
    '''
        #print(heatmap_dump.processes[1].summodules)
    ListOfPages= [[] for i in range(len(list_modules))]
    L=[[],[],[]]

    for pr in heatmap_dump.processes:
        pr.summodules=[0]*len(list_modules)
        #print(len(list_modules))
        counter=0
        for mod in pr.modules:
           #print(mod.name)
           index=get_index(list_modules,mod.name)
           if(index!=-1):
               counter=counter+1
               #print("module: "+mod.name+" has " +str(len(mod.pages)) +" pages and size of " + str(int(mod.size,0)))
               #time.sleep(5)
               # How many pages percent %

               pr.summodules[index]= len(mod.pages)*4096/int(mod.size,0) #Here you should sum all sizes 
               ListOfPages[index].extend(mod.pages)
               #ListOfPages[index]=(mod.pages)
               #print(ListOfPages)
               #print(ListOfPages[index][0].address)

               #print(str(pr.summodules[index])+" len: "+str(len(str(pr.summodules[index]))) )
               if(len(str(pr.summodules[index]))>4):
                   pr.summodules[index]=float(str(pr.summodules[index])[:6])*100
               #print(pr.summodules[index])
               #time.sleep(2)
        #print(len(ListOfPages))

    #duplicates
    #for item in ListOfPages:
        #item=list(tz.unique(item, key=lambda x: x.address))

    for item in list_modules:
        print(item.name)
    for item in list_modules:
        print(item.base)
    time.sleep(5)
    for i in range(0,len(ListOfPages)):
        ListOfPages[i]=list(tz.unique(ListOfPages[i], key=lambda x: x.address))

    '''
    for item in ListOfPages[283]:
        print(item.address)
    '''

    for pr in heatmap_dump.processes:
        for mod in pr.modules:
            index=get_index(list_modules,mod.name)
            flag="NO"
            if(index!=-1):
                if(int(mod.size,0)>=len(ListOfPages[index])*4096):
                    flag="YES"
                else:
                    print(mod.name+"-"+str(int(mod.size,0))+" - "+str(len(ListOfPages[index])*4096)+" "+flag+" "+str(index))


    #for item in ListOfPages[6]:
    #    print(item.address)
    #
    print("process")
    #for item in ListOfPages[6]:
    #    print(item.address)


    #print(ListOfPages[index][0].address)
    print("PAUSING")
    time.sleep(5)



    memmap.display_summaryheatmap(heatmap_dump,list_modules)

 
