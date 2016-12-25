import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import time
import process as pr

class MemoryDump:

    def __init__(self, path):
        self.path = path
        self.processesCount = 0
        self.processes = []    
    
    def cashing_of_processes(self):
        list_of_processes=pandas.read_fwf(co.output_location+"\pslist.info")
        for i in range(1,len(list_of_processes)):
            process=pr.Process(list_of_processes.iloc[i,1],list_of_processes.iloc[i,2])
            self.processes.append(process)
        self.processesCount=len(self.processes)
        print("Processes cashing (2/2) done!")
    
    def vol_pslist(self):
        f = open(co.output_location+"\pslist.info", "w")
        Command=co.volatility_standalone_location+" -f "+co.dump_memory_location+" --profile=Win7SP1x64 pslist"
        subprocess.call(Command,stdout=f)
        print("Processes cashing (1/2) done!")

    def vol_memmap(PID):
        f = open(co.output_location+"\memmap"+"_"+str(PID)+".info", "w")
        Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 memmap -p " + str(PID)
        subprocess.call(Command,stdout=f)
        print("memmap for PID:"+str(PID)+" is done!")

    def vol_dlllist(PID):
        f = open(co.output_location+"\dlllist"+"_"+str(PID)+".info", "w")
        Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 dlllist -p " + str(PID)
        subprocess.call(Command,stdout=f)
        print("dlllist for PID:"+str(PID)+" is done!")

    def add_process(self, process):
        self.processes.append(process)

