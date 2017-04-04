import mmap
import configuration as co
import entropy
import hashlib

start=0x0
size=0x0
def read_write_chunks(start, size):
    """
    Partition the memory and write it to a specific location
    """
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
    """
    Search for a special value in the memory dump
    """
    with open(co.dump_memory_location, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        x= mm.rfind(word,0,2147418112)
        print (x)
        print (hex(x))
        mm.close()

def slicing(start, size):
    """
    Calculate the number of Ascii, non-Ascii and number characters in addition to the entropy value for a memory chunk 
    """
    with open(co.dump_memory_location, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        mm.seek(int(start,16))
        rawdata= mm.read(int(size,16))
        a=0
        b=0
        c=0
        for c in rawdata:
           if(c<=31 or c==127):
              a=a+1
           elif(c<=57 or c>=48):
              b=b+1
           else:
              c=c+1
        e=entropy.entropy_c(rawdata)
        hash=hashlib.sha224(rawdata).hexdigest()
        return [c,a,b,e,hash]
        mm.close()
        
