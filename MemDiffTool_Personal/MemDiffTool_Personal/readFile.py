import hexdump
import pandas
import time
import numpy as np
import os
from bokeh.charts import HeatMap, output_file, show


'''
with open("F:\\MemoryDumps\\RamCapturer\\New\\A\\20161029.mem") as infile:
    counter=5
    for line in infile:
        if(counter<10):
            print(line)
            counter+=1
'''
# "C:\Users\ali-d\Desktop\Work\20161029.mem"

'''
#Working

with open("C:\\Users\\ali-d\\Desktop\\Work\\20161029.mem", "rb") as f:
    byte = f.read(1)
    c = open('output.txt', 'wb')
    while byte != b"":
        # Do stuff with byte.
        byte = f.read(1)
        print(byte)
        c.write(byte)
    c.close()

'''

'''
#Byte by Byte
start_time = time.time()
with open("C:\\Users\\ali-d\\Desktop\\Work\\20161029.mem", "rb") as f:
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        byte = f.read(1)

print("DON")
print("--- %s seconds ---" % (time.time() - start_time))
'''

#Line by Line
start_time = time.time()
def readnwriteDump():
    with open("C:\\Users\\ali-d\\Desktop\\Work\\20161029.mem","rb") as FileObj:
        #C:\Users\ali-d\Desktop\Work
        c = open('C:\\Users\\ali-d\\Desktop\\Work\\TEST.BAK', 'wb')
        for lines in FileObj:
            c.write(lines)
            #for i in range(len(lines)):
                #x=lines[0]

print("DON")
print("--- %s seconds ---" % (time.time() - start_time))



#Bokeh

# (dict, OrderedDict, lists, arrays and DataFrames are valid inputs)

'''
with open("C:\\Users\\ali-d\\Desktop\\Work\\TEST.BAK", "rb") as f:
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        #print("Hex Val is {0}, Decimal Val is {1}, Binary Val is {2}".format(hex(byte),byte,bin(byte)))
        print(byte)
        byte = f.read(1)
'''




bytesVal=[]
def openFile():
    with open("C:\\Users\\ali-d\\Desktop\\Work\\TEST.BAK","rb") as FileObj:
        for lines in FileObj:
            for i in range(len(lines)):
                #print("Hex Val is {0}, Decimal Val is {1}, Binary Val is {2}".format(hex(lines[i]),lines[i],bin(lines[i])))
                bytesVal.append(lines[i])
  
#for i in range(len(bytesVal)):
    #print(bytesVal[i])

Mito=[1,23,13,42,6,2,6,48,9,6,5,4,4,5,6,7,28,9,0,4,2,3,4,25,6,7,5,6,8,3,2,3,20,40,30,22,33,44,2,3,1,41,25,23,15,16,17,34,23,63,24,34,34]
print(list(range(9)))
data = {'bytes': ['bytes']*len(Mito)   ,
        'byte_val': Mito,
        'Y': list(range(len(Mito)))}

hm = HeatMap(data, x='bytes', y='Y', values='byte_val',
             title='DataDump', stat=None)

output_file('heatmap.html')
show(hm)