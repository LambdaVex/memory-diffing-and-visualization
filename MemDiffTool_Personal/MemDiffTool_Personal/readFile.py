import hexdump
import pandas





'''
with open("F:\\MemoryDumps\\RamCapturer\\New\\A\\20161029.mem") as infile:
    counter=5
    for line in infile:
        if(counter<10):
            print(line)
            counter+=1
'''
# "C:\Users\ali-d\Desktop\Work\20161029.mem"

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



