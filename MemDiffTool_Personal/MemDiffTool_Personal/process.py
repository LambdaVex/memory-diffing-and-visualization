import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import module as md

class Process:

    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
        self.modules = []    
    
    def add_modules(self):
        process="dlllist_"+str(self.pid)+".info"
        dlllist=pandas.read_fwf(co.output_location+"\\"+process)

        if(len(dlllist)>2):
            for i in range(4,len(dlllist)):     
                line = dlllist.iloc[i,0]
                data = line.split() #split string into a list
                # Add check because sometimes the path is empty
                if len(data) > 3:
                    name=os.path.basename(os.path.normpath(data[3]))
                    if(name != "----" and name != "Path"):
                        module=md.Module(os.path.basename(os.path.normpath(data[3])) if len(data) > 3 else "n/a",data[0],data[1])       
                        self.modules.append(module)
                else:
                    module=md.Module("n/a",data[0],data[1])       
                    self.modules.append(module)
                        
                    
      