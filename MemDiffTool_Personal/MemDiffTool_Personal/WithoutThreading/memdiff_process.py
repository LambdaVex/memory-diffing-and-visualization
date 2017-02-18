import memory_dump as md
import configuration as co
import pandas
from bisect import *
from pandas import DataFrame
import time
import os
import xml_builder as xmlb
import xml_parser as xmlp
from multiprocessing import Process
import multiprocessing

start_time = time.time()
######## Initialize the Dump file
dump1 = md.MemoryDump(co.dump_memory_location)
######## Cash the processes of the Dump file
#dump1.vol_pslist() #Uncomment for New Dumps
dump1.cashing_of_processes()
######## Cash the modules of each process
# dump1.vol_dlllist() #Uncomment for New Dumps
dump1.cashing_of_modules()
######## Cash the pages of each module
#dump1.vol_memmap() #Uncomment for New Dumps
dump1.cashing_of_pages()

xmlb.build_file(dump1)
#xmlp.prase()
