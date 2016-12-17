import subprocess
import os
import pandas
import Configuration as co

volatilityLoc=co.volatility_standalone_location
dumpLoc=co.dump_memory_location

def vol_pslist():
    f = open(co.output_location, "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 pslist"
    subprocess.call(Command,stdout=f)
    print("pslist done!")

def vol_memmap(PID):
    f = open(co.output_location+str(PID)+".info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 memmap -p " + str(PID)
    subprocess.call(Command,stdout=f)
    print("memmap for PID:"+str(PID)+" is done!")

def vol_dlllist(PID):
    f = open(co.output_location+str(PID)+".info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 dlllist -p " + str(PID)
    subprocess.call(Command,stdout=f)
    print("dlllist for PID:"+str(PID)+" is done!")


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
#vol_pslist()
pslist=pandas.read_fwf('DumpInfo\pslist.info')

# Print your PID list
#for i in range(len(pslist)):
#    print("{0}".format(pslist.iloc[i,2]))



for i in range(1,len(pslist)):
    vol_memmap(pslist.iloc[i,2])
    #print("{0}".format(pslist.iloc[i,2]))
#vol_memmap(4)

'''
file = open('memmap.txt', 'r')
content=file.read()
#print (content)
df3=pandas.read_fwf('memmap.txt')

myDict=dict()
#print(len(df3))
for i in range(len(df3)):
    #print("{0} -- {1}".format(df3.iloc[i,1],df3.iloc[i,2]))
    #myDict.update({df3.iloc[i,1]: df3.iloc[i,2]})
    myDict[df3.iloc[i,1]]=df3.iloc[i,2]

keylist = myDict.keys()
keylist.sort()
for i in range(len(keylist)):
    print ("{0} --- {1}".format(keylist[i],int(keylist[i], 16)))
'''