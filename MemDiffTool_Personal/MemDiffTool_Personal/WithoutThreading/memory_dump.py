import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import bisect_module as bi
import process as pr
import module as md
class MemoryDump:
    """
    memory_dump encapsulates a dump memory.
    """
    def __init__(self, path):#to remove threading uncomment the line below and comment the one below it
        """
        Construct a new 'memory_dump' object.

        :param path: The path of the memory dump
        :return: returns nothing
        """
        self.path = path
        self.processesCount = 0
        self.processes = []    
   
    ######## Processing Processes      
    def cashing_of_processes(self):
        """
        Cashes the processes.
        """
        list_of_processes=pandas.read_fwf(co.output_location+"\pslist.info")
        #change the range to 1,len(processes) to remove threading
        for i in range(1,len(list_of_processes)):
            process=pr.Process(list_of_processes.iloc[i,1],list_of_processes.iloc[i,2])
            self.processes.append(process)
        self.processesCount=len(self.processes)
        print("Processes cashing (2/2) done!")
    
    def invoking_pid_of_processes(self):
        """
        Invokes the process' ids.
        """
        list_pr=[]
        list_of_processes=pandas.read_fwf(co.output_location+"\pslist.info")
        for i in range(1,len(list_of_processes)):
            list_pr.append(list_of_processes.iloc[i,2])
        return list_pr

    def vol_pslist(self):
        """
        Invokes the processes running.
        """
        f = open(co.output_location+"\pslist.info", "w")
        Command=co.volatility_standalone_location+" -f "+co.dump_memory_location+" --profile=Win7SP1x64 pslist"
        subprocess.call(Command,stdout=f)
        print("Processes cashing (1/2) done!")
    
    ######## Processing Modules
    def cashing_of_modules(self):
        """
        Cashes the modules.
        """
        for i in self.processes:
            i.add_modules()
        print("Modules cashing (2/2) done!")

    def vol_dlllist(self):
        """
        Invokes the dlls running.
        """
        for i in self.processes:
            f = open(co.output_location+"\dlllist"+"_"+str(i.pid)+".info", "w")
            Command=co.volatility_standalone_location+" -f "+co.dump_memory_location+" --profile=Win7SP1x64 dlllist -p " + str(i.pid)
            subprocess.call(Command,stdout=f)
            print("dlllist for PID:"+str(i.pid)+" is done!")
        print("Modules cashing (1/2) done!")

    def invoke_vol_dlllist(self,Prs):
        """
        Invokes the dlls for special process.
        """
        for i in Prs:
            f = open(co.output_location+"\dlllist"+"_"+str(i)+".info", "w")
            Command=co.volatility_standalone_location+" -f "+co.dump_memory_location+" --profile=Win7SP1x64 dlllist -p " + str(i)
            subprocess.call(Command,stdout=f)
            print("dlllist for PID:"+str(i)+" is done!")
        print("Modules cashing (1/2) done!")
    ######## Processing Pages
    #all IDs
    def cashing_of_pages(self):
        """
        Cashes the pages.
        """
        for i in self.processes:
            print("Process: "+i.pid+" under process")
            for j in i.modules:
               #add the returned uncovered pages sizes per module 
               i.addUncoveredMemeoryFromModules(j.add_pages(i.pid))
            i.calulateUncoveredMemroy()
        print("Modules cashing (2/2) done!")

    #single ID  
    def cashing_of_pid_pages(self,process):
        """
        Invokes the pages for special process.
        """
        for i in process.modules:
            i.add_pages(process.pid)
        print("Modules cashing (2/2) done!") 

    def vol_memmap(self):
        """
        Invokes the pages running.
        """
        for i in self.processes:
            f = open(co.output_location+"\memmap"+"_"+str(i.pid)+".info", "w")
            Command=co.volatility_standalone_location+" -f "+co.dump_memory_location+" --profile=Win7SP1x64 memmap -p " + str(i.pid)
            subprocess.call(Command,stdout=f)
            print("memmap for PID:"+str(i.pid)+" is done!")
        print("Pages cashing (1/2) done!")

    def invoke_vol_memmap(self,Prs):
        """
        Invokes the pages for special process.
        """
        for i in Prs:
            f = open(co.output_location+"\memmap"+"_"+str(i)+".info", "w")
            Command=co.volatility_standalone_location+" -f "+co.dump_memory_location+" --profile=Win7SP1x64 memmap -p " + str(i)
            subprocess.call(Command,stdout=f)
            print("memmap for PID:"+str(i)+" is done!")
        print("Pages cashing (1/2) done!")
    ######## Output
    def show_modules_in_processes(self):
        for i in self.processes:
            print("Process "+i.name+" has "+str(len(i.modules))+" modules")