import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import module as md
import bisect_module as bi

class Process:

    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
        self.memory_used_by_modules=0
        self.memory_used_by_pages=0
        self.modules = []    
        self.summodules = []

    def add_modules(self):
        #this section to calculate the memory used by pages for a certain process
        memmap=pandas.read_fwf(co.output_location+"\memmap_"+self.pid+".info",colspecs=[(0,18),(19,37),(38,56),(57,75)])
        #the size of memory used
        sizes=memmap.ix[:,2]
        virtual=memmap.ix[:,0]
        #dicard the first two lines
        virtual=virtual[2:]
        sizes=sizes[2:]
        #first index of core adresse 
        for i in virtual:
            if(int(i,16)>int('0x000007ff00000000',16)):
                jump=bi.index(virtual,i)
                break;
        #the sum of pages sizes till the jump minus the first two line discarded
        self.memory_used_by_pages=sum(int(i,16) for i in sizes[:jump])

        process="dlllist_"+str(self.pid)+".info"
        dlllist=pandas.read_fwf(co.output_location+"\\"+process)

        if(len(dlllist)>2):
            for i in range(4,len(dlllist)):     
                line = dlllist.iloc[i,0]
                #print(line)
                data = line.split() #split string into a list
                #print(data)
                # Add check because sometimes the path is empty
                if len(data) > 3:
                    #os.posixpath 
                    name=os.path.basename(os.path.normpath(data[3]))
                    if(name != "----" and name != "Path"):
                        # A fix for the bug when the data is not in the last index of data 
                        module=md.Module(os.path.basename(os.path.normpath(data[len(data)-1])) if len(data) > 3 else "n/a",data[0],data[1])
                        #sum the number of memory used by the Dlls  
                        self.memory_used_by_modules=self.memory_used_by_modules+ int(data[1],16)  
                        #print(module.name)
                        self.modules.append(module)
                else:
                    module=md.Module("n/a",data[0],data[1])       
                    self.modules.append(module)
                      
          