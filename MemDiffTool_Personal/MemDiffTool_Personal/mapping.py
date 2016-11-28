import mmap
start=0x0
size=0x0
def read_write_chunks(start, size):
    with open("D:\\Dump\\A\\dump.mem", "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        mm.seek(start)
        with open("D:\\Dump\\A\\pid340.mem", "wb") as s:
            s.write(mm.read(size))
        mm.seek(start)
        print mm.read(size)
        print "Done successfully"
        mm.close()

def search(word):
    with open("D:\\Dump\\A\\dump.mem", "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        x= mm.rfind(word,0,2147418112)
        print x
        print hex(x)
        mm.close()


#read_write_chunks(0x4a680000,0x6000)
search("csrss.exe")

"""
*check LoadCount in pslist
*check memmap,memdump
"""