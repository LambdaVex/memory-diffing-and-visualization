import memory_dump as md
import configuration as co
import pandas
from bisect import *
from pandas import DataFrame
import time

#### Initialize the Dump file
dump1 = md.MemoryDump(co.dump_memory_location)

#### Cash the processes
# dump1.vol_pslist() #Uncomment for New Dumps
dump1.cashing_of_processes()

print(dump1.processesCount)



