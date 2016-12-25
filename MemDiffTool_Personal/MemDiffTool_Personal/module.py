import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import bisect_module as bi
import time
import page as pg
class Module:

    def __init__(self, name, base,size):
        self.name = name
        self.base = base
        self.size = size
        self.pages = []    
        #252

    def add_pages(self,pid):
        print(pid+" "+self.base)
        memmap=pandas.read_fwf(co.output_location+"\memmap_"+pid+".info",widths=[18,18,18,18])
        virtual_address=memmap.ix[:,0]
        #print(virtual_address)
        page=bi.index(virtual_address,self.base)
        print(page)
       # print(virtual_address[page])
        if(page != -1):
            while int(virtual_address[page],16)<=int(self.base,16)+int(self.size,16):
                newPage=pg.Page(virtual_address[page],"print_Ascci","non_print_Ascci","print_Ascci_Num")
                self.pages.append(virtual_address[page])
                print(virtual_address[page]+"Added!")
                page=page+1
           # time.sleep(5)