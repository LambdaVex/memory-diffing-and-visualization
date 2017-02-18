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

def seq(start):
    start_time = time.time()
    ######## Initialize the Dump file
    dump1 = md.MemoryDump(co.dump_memory_location,start)
    ######## Cash the processes of the Dump file
    dump1.cashing_of_processes()
    ######## Cash the modules of each process
    dump1.cashing_of_modules()
    ######## Cash the pages of each module
    dump1.cashing_of_pages()
    xmlb.build_file(dump1)
    print("--- %s seconds for a thread ---" % (time.time() - start_time))

if __name__ == '__main__':
        start_time_for_all = time.time()
        pool = multiprocessing.Pool(3) 
        pool.map(seq, ['1','14','27'])
        print("--- %s seconds_for_the_whole_program ---" % (time.time() - start_time_for_all))
        xmlb.combine_xml(['testxml_withthread_number_1.xml','testxml_withthread_number_14.xml','testxml_withthread_number_27.xml'])
        print("Final Xml file is ready")

#to remove threading only run the code below
#below is the flow without threading
"""

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

"""





'''
for i in dump1.processes:
    print("{0}::{1}".format(i.pid,len(i.modules)))
'''