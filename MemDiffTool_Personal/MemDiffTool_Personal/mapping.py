import mmap
import configuration as co
import entropy

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
        mm.seek(int(start,16))
        rawdata= mm.read(int(size,16))
        a=0
        b=0
        c=0
        rawdata_S=''
        for c in rawdata:
           rawdata_S=rawdata_S+str(c)
           if(c<=31 or c==127):
              a=a+1
           elif(c<=57 or c>=48):
              b=b+1
           else:
              c=c+1
        e=entropy.entropy_c(rawdata_S)
        #print("the entropy is={0}".format(e))
        return [c,a,b,e]
        mm.close()
        

#read_write_chunks(0x4a680000,0x6000)
#slicing('0x0000000100000000','0x5f000')
#print(int('0x0000000100000000',16))

"""
*check LoadCount in pslist
*check memmap,memdump
"""
