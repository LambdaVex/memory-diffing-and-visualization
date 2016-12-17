import mmap
import configuration as co

start=0x0
size=0x0
def read_write_chunks(start, size):
    with open(co.output_location+"\chunk.info", "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        mm.seek(start)
        with open(co.dump_memory_location, "wb") as s:
            s.write(mm.read(size))
        mm.seek(start)
        print mm.read(size)
        print "Done successfully"
        mm.close()

def search(word):
    with open(co.dump_memory_location, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        x= mm.rfind(word,0,2147418112)
        print x
        print hex(x)
        mm.close()

def slice(start, size):
    with open(co.dump_memory_location, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        #print "Initial place of the pointer:"+str(mm.tell())+" in heximal it would be:"+str(hex(mm.tell()))
        mm.seek(start)
        print "First addresse of the pointer:"+str(mm.tell())+" in heximal it would be:"+str(hex(mm.tell()))
        #with open("D:\\Dump\\A\\pid340.mem", "wb") as s:
        #    s.write(mm.read(size))
        #mm.seek(start)
        mm.read(size)
        print "Last addresse of the pointer:"+str(mm.tell())+" in heximal it would be:"+str(hex(mm.tell()))
        print "Done successfully"
        mm.close()
        

#read_write_chunks(0x4a680000,0x6000)
slice(0x0000000048580000,0x20000)

"""
*check LoadCount in pslist
*check memmap,memdump
"""