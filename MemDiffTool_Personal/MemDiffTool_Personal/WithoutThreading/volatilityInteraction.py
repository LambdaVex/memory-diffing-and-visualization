import subprocess
import os
import pandas
import configuration as co

volatilityLoc=co.volatility_standalone_location
dumpLoc=co.dump_memory_location

def vol_pslist():
    """
    Invoke processes list from the memory dump.
    """
    f = open(co.output_location+"\pslist.info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 pslist"
    subprocess.call(Command,stdout=f)
    print("pslist done!")

def vol_memmap(PID):
    """
    Invoke pages from the memory dump.
    """
    f = open(co.output_location+"\memmap"+"_"+str(PID)+".info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 memmap -p " + str(PID)
    subprocess.call(Command,stdout=f)
    print("memmap for PID:"+str(PID)+" is done!")

def vol_dlllist(PID):
    """
    Invoke dlls list from the memory dump.
    """
    f = open(co.output_location+"\dlllist"+"_"+str(PID)+".info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 dlllist -p " + str(PID)
    subprocess.call(Command,stdout=f)
    print("dlllist for PID:"+str(PID)+" is done!")

def vol_memdump(PID):
    """
    Invoke all memory resident pages in a process from the memory dump.
    """
    f = open(co.output_location+"\memdump"+"_"+str(PID)+".info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 memdump -p " + str(PID) +" -D "+co.output_location+"\DumpFolder"
    subprocess.call(Command,stdout=f)
    print("memdump for PID:"+str(PID)+" is done!")


def vol_new(PID):
    """
    Invoke all memory resident pages in a process from the memory dump.
    """
    f = open(co.output_location+"\memdump"+"_"+str(PID)+".info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 memdump -p " + str(PID) +" -D "+co.output_location+"\DumpFolder"
    subprocess.call(Command,stdout=f)
    print("memdump for PID:"+str(PID)+" is done!")

def processMemory(infile):
    df3=pandas.read_fwf(infile)
    for i in range(len(df3)):   
        if(df3.iloc[i,0][0]=='0'):
            #print(df3.iloc[i,0][0])
            hexVal=df3.iloc[i,0][2:]
            decVal=int(hexVal, 16)
            bitVal=bin(decVal)
           # print("{0}".format(bitVal))
            print("{0} --> {1} --> {2}".format(df3.iloc[i,0],decVal,bitVal))


# First Obtain pslist
vol_pslist()
pslist=pandas.read_fwf(co.output_location+"\pslist.info")
#pslist=pandas.read_fwf('DumpInfo\pslist.info')

# Print your PID list
#for i in range(len(pslist)):
#    print("{0}".format(pslist.iloc[i,2]))

#vol_new(280)

for i in range(1,len(pslist)):
    vol_dlllist(pslist.iloc[i,2])
    vol_memmap(pslist.iloc[i,2])
    #vol_memdump(pslist.iloc[i,2])
#for i in range(1,len(pslist)):
#    vol_memmap(pslist.iloc[i,2])
    #print("{0}".format(pslist.iloc[i,2]))
#vol_memmap(4)

