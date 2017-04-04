import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import module as md
import bisect_module as bi

class Process:
    """
    Process encapsulates the process.
    """
    P_indicator=-100

    ratio=0
    def __init__(self, name, pid,covered_memory_by_pages=0 ,covered_memory_by_modules=0 ,ratio=0 ):
        """
        Construct a new 'Process' object.

        :param name: The name of the process
        :param pid: The id of the process
        :param covered_memory_by_pages: The size of covered memory by pages
        :param covered_memory_by_modules: The size of covered memory by modules
        :param ratio: The size of uncovered memory
        :return: returns nothing
        """
        self.name = name
        self.pid = pid
        self.modules = []    
        self.summodules = []
        self.covered_memory_by_pages=0
        self.covered_memory_by_modules=0
        self.ratio=0
      
    def calulateUncoveredMemroy(self):
        """
        Calculate the uncovered memory.
        """
        if self.covered_memory_by_pages!=0:
            self.ratio=(round((self.covered_memory_by_pages-self.covered_memory_by_modules)/self.covered_memory_by_pages, 2))*100
        else:
            self.ratio=-1
          
    def addUncoveredMemeoryFromModules(self,memory):
        """
        Add the sizes of the modules.
        """
        self.covered_memory_by_modules=self.covered_memory_by_modules+int(memory,16)

    def add_modules(self):
        """
        Add the related modules.
        """
        #this section to calculate the memory used by pages for a certain process
        memmap=pandas.read_fwf(co.output_location+"\memmap_"+self.pid+".info",colspecs=[(0,18),(19,37),(38,56),(57,75)])
        #the size of memory used
        sizes=memmap.ix[:,2]
        virtual=memmap.ix[:,0]
        #dicard the first two lines
        virtual=virtual[2:]
        sizes=sizes[2:]
        #initialization
        jump=-1
        #first index of core adresse 
        for i in virtual:
            if(int(i,16)>int('0x0000080000000000',16)):
                try:
                    jump=bi.index(virtual,i)
                except:
                    jump=-2
                    break;
                break;
        #the sum of pages sizes till the jump minus the first two line discarded
        if(jump>-1):
             self.covered_memory_by_pages=sum(int(i,16) for i in sizes[:jump-1])
        if(jump==-2):
             self.covered_memory_by_pages=-1
        process="dlllist_"+str(self.pid)+".info"
        dlllist=pandas.read_fwf(co.output_location+"\\"+process)
        if(len(dlllist)>2):
            for i in range(4,len(dlllist)):     
                line = dlllist.iloc[i,0]
                if not (pandas.isnull(line)):
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
                            #self.memory_used_by_modules=self.memory_used_by_modules+ int(data[1],16)  
                            #print(module.name)
                            self.modules.append(module)
                    else:
                        module=md.Module("n/a",data[0],data[1])       
                        self.modules.append(module)
                      
          