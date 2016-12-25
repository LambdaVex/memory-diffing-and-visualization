import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import bisect_module as bi
import time
class Module:

    def __init__(self, name, base,size):
        self.name = name
        self.base = base
        self.size = size
        self.pages = []    
        #252
    def add_pages(self,pid):
        print(pid+" "+self.base)
        memmap=pandas.read_fwf(co.output_location+"\memmap_252B.info",widths=[18,18,18,18])
        virtual_address=memmap.ix[:,0]
        print(len(virtual_address))
        print(virtual_address)
        #page=bi.index(virtual_address,self.base)
        #print(page)
        time.sleep(5)