import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import mapping
import time
import sys



def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    print("if {0} != {1} and {2} == {3}:\n".format(i,len(a),a[i],x))
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

def write_cash(process_name_virtual_addresses,process_id,heatmap_draw_statistics):
    f = open(co.output_location+"\cashing\\"+process_id+".info", "w")# w means Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. for more info https://www.tutorialspoint.com/python/python_files_io.htm
    f.write("The Process name={0} its ID is ={1}\n".format(process_name_virtual_addresses[0],process_id))
    for i in range(1,len(process_name_virtual_addresses)):#then put i to begin from 1
        f.write(process_name_virtual_addresses[i])
        f.write('\t'+".\cashing\\rawdata\\"+process_id+"_"+process_name_virtual_addresses[i]+'.data\t')
        f.write(heatmap_draw_statistics[2])
        f.write('\n')
    f.close()
    f1 = open(co.output_location+"\cashing\\rawdata\\"+process_id+"_"+process_name_virtual_addresses[0]+".info", "wb")# w means Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. for more info https://www.tutorialspoint.com/python/python_files_io.htm
    f.write(heatmap_draw_statistics[1])
    f1.close()

pslist=pandas.read_fwf(co.output_location+"\pslist.info")
jj=0
for i in range(1,len(pslist)):
       print(pslist.iloc[i,2])##ps list ID at specific i
       virtual_address=[]
       physical_address=[]
       memmap=pandas.read_fwf(co.output_location+"\memmap_"+pslist.iloc[i,2]+".info",widths=[18,18,18,18])
       dlllist=pandas.read_fwf(co.output_location+"\dlllist_"+pslist.iloc[i,2]+".info",widths=[18,18,18,18])
       if(dlllist.ix[1,0]=='Unable to read PEB'):
           continue
       #try:
       #except:
       #     continue
        # converts the table to list 
       virtual_address=memmap.ix[:,0]
       print(virtual_address)
       physical_address=memmap.ix[:,1]
       print(len(dlllist))
       for i in range(0,len(dlllist)-6):
               line = dlllist.iloc[i,:]
               print("dlllist.iloc[i,:]={0},i is {1}".format(dlllist.iloc[i,:],i))
               data = line.split() #split string into a list
               sys.exit("Error message")
               Base=data[0]
               Size=data[1]
               Path=os.path.basename(os.path.normpath(data[3]))
               #print("Base= {0} size= {1} path= {2} <from dlllist plug in>".format(Base,Size,Path))
               slice=[Path]
               heatmap_draw_statistics=[Path]
               #print(virtual_address)
               print(Base)
               #search for the addresse in memmap equal to Base and name it page
               page=index(virtual_address,Base)
               #print("The index of first address matched between virtual address <from memmap> and Base address <from dlllist> is ({0})>".format(page))
               #print("First Vitual address matched is ={0}".format(virtual_address[page]))
               time.sleep(5.5) 

               #slice.insert(len(slice),mapping.slicing(Base,Size))
               while int(virtual_address[page],16)<=int(Base,16)+int(Size,16):
                   #print("Enter loop")
                   #print("while {0}<={1}+{2}".format(virtual_address[page],Base,Size))
                   slice.insert(len(slice),virtual_address[page])
                   heatmap_draw_statistics.insert(len(heatmap_draw_statistics),mapping.slicing(physical_address[page],'0x1000'))
                   #mapping with statistics
                   #next page from memmap
                   page=page+1
               for c in heatmap_draw_statistics[1]:
                    if(c<=31 or c==127):
                            non_printable_ASCI=non_printable_ASCI+1
                    else:
                            printable_ASCII=printable_ASCII+1
               heatmap_draw_statistics.insert(len(heatmap_draw_statistics),[non_printable_ASCI,printable_ASCII])
               write_cash(slice,pslist.iloc[i,2],heatmap_draw_statistics)


#write_cash("SKype.exe","568",['52525','225625','565636'],['125','98','789'],'sdfsdf')
