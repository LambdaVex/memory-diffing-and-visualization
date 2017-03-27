import memory_dump as md
import configuration as co
import pandas
from bisect import *
from pandas import DataFrame
import time
import os
import xml_builder as xmlb
#import xml_parser as xmlp
import visualize_memory as xmlp
from multiprocessing import Process
import multiprocessing

start_time = time.time()

######## Volatility ########
dump1 = md.MemoryDump(co.dump_memory_location)
'''
dump1.vol_pslist()
list_pr=dump1.invoking_pid_of_processes()
print("pslist Done!")
dump1.invoke_vol_dlllist(list_pr)
print("dlllist Done!")
dump1.invoke_vol_memmap(list_pr)
print("memmap Done!")
#time.sleep(5)
'''

######## Initialize the Dump file
######## Cash the processes of the Dump file
#dump1.vol_pslist() #Uncomment for New Dumps
dump1.cashing_of_processes()
######## Cash the modules of each process
#dump1.vol_dlllist() #Uncomment for New Dumps
dump1.cashing_of_modules()
######## Cash the pages of each module
#dump1.vol_memmap() #Uncomment for New Dumps
dump1.cashing_of_pages()

xmlb.build_file(dump1)

#xmlp.parse()
