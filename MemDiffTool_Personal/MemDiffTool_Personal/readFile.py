import hexdump
import pandas
import time
import numpy as np
import os



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
with open("C:\\Users\\ali-d\\Desktop\\Work\\20161029.mem","rb") as FileObj:
    #C:\Users\ali-d\Desktop\Work
    c = open('C:\\Users\\ali-d\\Desktop\\Work\\TEST.BAK', 'wb')
    for lines in FileObj:
        c.write(lines)
        #for i in range(len(lines)):
            #x=lines[0]

print("DON")
print("--- %s seconds ---" % (time.time() - start_time))


