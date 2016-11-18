import mmap

def openDumpFile(filename):
    with open(filename, "r+b") as f:
        map = mmap.mmap(f.fileno(), 0)
        print("Dump File Opened...")
        return map

def closeDumpFile(map):
    print("Closing Dump File...")
    map.close()

    
'''
To use these functions just import them as the following to your file:
from mmapOP import openDumpFile, closeDumpFile
'''