import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import bisect_module as bi
import time
import page as pg
import mapping
class Module:


    M_indicator=-100

    def __init__(self, name, base, size):
        self.name = name
        self.base = base
        self.size = size
        self.memory_used_by_pages=0
        self.pages = []    
        self.hmpages = [] 
        #252

    def add_pages(self,pid):
        #print(pid+" "+self.base)
        memmap=pandas.read_fwf(co.output_location+"\memmap_"+pid+".info",colspecs=[(0,18),(19,37),(38,56),(57,75)])
        virtual_address=memmap.ix[:,0]
        physical_address=memmap.ix[:,1]
        #the size of memory used
        sizes=memmap.ix[:,2]
        #the sum of pages sizes
        #self.memory_used_by_pages=sum(int(i,16) for i in sizes[2:])
        #page_size=memmap.ix[:,2].replace(" ", "")
        #print(virtual_address)
        page=bi.index(virtual_address,self.base)
  
        if(page != -1):
            while int(virtual_address[page],16)<=int(self.base,16)+int(self.size,16):
                #MHDCODE
                statistics=mapping.slicing(physical_address[page],sizes[page])
                #newPage=pg.Page(virtual_address[page],statistics[0],statistics[1],statistics[2])
                newPage=pg.Page(virtual_address[page],statistics[0],statistics[1],statistics[2],statistics[3],sizes[page],statistics[4],0)
                self.pages.append(newPage)
                #self.pages.append(virtual_address[page])
                #print(virtual_address[page]+"Added!")
                page=page+1
        #time.sleep(5)
