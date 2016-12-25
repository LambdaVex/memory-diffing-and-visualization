import mmap
import configuration as co

start=0x0
size=0x0
def read_write_chunks(start, size):
    with open(co.output_location+"\chunk.info", "w") as f:# w means Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. for more info https://www.tutorialspoint.com/python/python_files_io.htm
        mm = mmap.mmap(f.fileno(), 0)
        mm.seek(start)
        with open(co.dump_memory_location, "wb") as s:
            s.write(mm.read(size))
        mm.seek(start)
        print (mm.read(size))
        print ("Done successfully")
        mm.close()

def search(word):
    with open(co.dump_memory_location, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        x= mm.rfind(word,0,2147418112)
        print (x)
        print (hex(x))
        mm.close()

def slicing(start, size):
    with open(co.dump_memory_location, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        #print (start)
        #print (size)
        #print "Initial place of the pointer:"+str(mm.tell())+" in heximal it would be:"+str(hex(mm.tell()))
        #print (int(start,16))
        mm.seek(int(start,16))
        #print ("First addresse of the pointer:"+str(mm.tell())+" in heximal it would be:"+str(hex(mm.tell())))
        #with open("D:\\Dump\\A\\pid340.mem", "wb") as s:
        #    s.write(mm.read(size))
        #mm.seek(start)
        return mm.read(int(size,16))
        #print(mm.read(int(size,16)))
        #print ("Last addresse of the pointer:"+str(mm.tell())+" in heximal it would be:"+str(hex(mm.tell())))
        #print ("Done successfully")
        mm.close()
        

#read_write_chunks(0x4a680000,0x6000)
#slicing('0x0000000100000000','0x5f000')
#print(int('0x0000000100000000',16))

"""
*check LoadCount in pslist
*check memmap,memdump
"""