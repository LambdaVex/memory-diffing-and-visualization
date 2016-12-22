import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import time

volatilityLoc=co.volatility_standalone_location
dumpLoc=co.dump_memory_location


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def vol_pslist():
    f = open(co.output_location+"\pslist.info", "w")
    Command=volatilityLoc+" -f "+dumpLoc+" --profile=Win7SP1x64 pslist"
    subprocess.call(Command,stdout=f)
    print("pslist done!")

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



"""
X=memmap.iloc[5,0]
print(X)
print(type(X))
hex_int = int(X, 16)
print(hex_int)
print(type(hex_int))

"""

memmap=pandas.read_fwf(co.output_location+"\memmap_280.info")
dlllist=pandas.read_fwf(co.output_location+"\dlllist_280.info")

# converts the table to list 
virtual_address=memmap.ix[:,0]

for i in range(5,len(dlllist)):
       line = dlllist.iloc[i,0]
       data = line.split() #split string into a list
       Base=data[0]
       Size=data[1]
       Path=os.path.basename(os.path.normpath(data[3]))
       print("Base= {0} size= {1} path= {2}".format(Base,Size,Path))
       slice=[Path]

       #search for the addresse in memmap equal to Base and name it page
       page=index(virtual_address,Base)
       print(page)
       print(virtual_address[page])
       time.sleep(5.5) 
       while int(virtual_address[page],16)<=int(Base,16)+int(Size,16):
           print("Enter loop")
           print("while {0}<={1}+{2}".format(virtual_address[page],Base,Size))
           slice.insert(len(slice),virtual_address[page])
           #next page from memmap
           page=page+1
            
       #write this slice 
       #draw this slice


# this converts the panda to list 
#List=memmap.ix[:,0]
#print(List[len(List)-1])


#print(index(List,"0x0000ffffffd0e000"))

#Col1=memmap.iloc[:0]
#print(Col1)

#T=DataFrame(memmap)



#print(T)


#print(memmap.iloc[4,0])

'''
for i in range(2,len(memmap)):
    Val=memmap.iloc[i,0]
    #Val2=int(Val, 16)
    print("{0} --> {1} --> {2}".format(memmap.iloc[i,0],memmap.iloc[i,2],int(Val, 16)))
'''

    #hex_int = int(pslist.iloc[i,0], 16)
    #print("{0} ".format(type(pslist.iloc[i,0])))
   
    #hex_int = int(pslist.iloc[i,0], 16)
    #decVal=int(ord(hexVal), 16)
    
    #hexVal=pslist.iloc[i,0]
    #print("{0} ".format(int(hexVal, 16)))

