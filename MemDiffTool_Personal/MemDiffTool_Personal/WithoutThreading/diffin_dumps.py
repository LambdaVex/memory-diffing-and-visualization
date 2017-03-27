import heatmap_processess as phmap
import heatmap_MemoryDump as memmap
import math
import pandas
import memory_dump as md
import process as pr
import module as mod
import page as pge
import xml_parser as xp
import configuration as co
import heatmap_diffing as hmapdiff
import time

filename_1="Resources/DiffingXml/NewFinal/FCA.xml"
filename_2="Resources/DiffingXml/NewFinal/TCA.xml"
   
dump_A=xp.parse(md.MemoryDump("heatmap1"),filename_1)
dump_B=xp.parse(md.MemoryDump("heatmap2"),filename_2)
dump_Diff = md.MemoryDump("DIFF")

"""Create a list of processes in dump_A.
If a process in dump_B doesn't appear in dump_A, then assign the tag 1 (New)
"""
pid_listA = {process.pid for process in dump_A.processes}
for process in dump_B.processes:
    if process.pid not in pid_listA:
        #print (process.pid )
        process.P_indicator=1
        dump_Diff.processes.append(process)
"""Create a list of processes in dump_B.
If a process in dump_A doesn't appear in dump_B, then assign the tag -1 (Deleted)
"""
pid_listB = {process.pid for process in dump_B.processes}
for process in dump_A.processes:
    if process.pid not in pid_listB:
        #print (process.pid )
        process.P_indicator=-1
        dump_Diff.processes.append(process)
"""Other processes will have the value of -100 for further processing"""
for i in dump_A.processes:
    if(i.P_indicator==-100):
        dump_Diff.processes.append(i)
for i in dump_B.processes:
    if(i.P_indicator==-100):
        dump_Diff.processes.append(i)

hmapdiff.display_diffingheatmap(dump_Diff,dump_A,dump_B)
print("Done")




'''
print(len(dump_A.processes))
print(len(dump_B.processes))
print(len(dump_Diff.processes))
for i in dump_A.processes:
    if(i.P_indicator==-100):
        proc = next((x for x in dump_B.processes if x.pid == i.pid), None)
        diffProcesses(i,proc)
        print(proc.memory_used_by_pages)
#for i in dump_Diff.processes:
#    print(i.P_indicator)

for i in dump_A.processes:
    print(i.P_indicator)
'''


'''
def diffProcesses(Proc_A,Proc_B):
    """Create a list of modules in Proc_A.
    If a module in Proc_B doesn't appear in Proc_A, then assign the tag 1 (New)
    The process is repeated for modules in Proc_B
    """
    base_listA = {module.base for module in Proc_A.modules}
    for module in Proc_B.modules:
        if module.base not in base_listA:
            module.M_indicator=1

    base_listB = {module.base for module in Proc_B.modules}
    for module in Proc_A.modules:
        if module.base not in base_listB:
            module.M_indicator=-1

def diffModules(Module_A,Module_B):
    address_listA = {page.address for page in Module_A.pages}
    for page in Module_B.pages:
        if page.address not in address_listA:
            #print (process.pid )
            page.Page_indicator=1
            #dump_Diff.processes.append(process)

    #print("Deleted Processes")
    address_listB = {page.address for page in Module_B.pages}
    for page in Module_A.pages:
        if page.address not in address_listB:
            #print (process.pid )
            page.Page_indicator=-1
            #dump_Diff.processes.append(process)
'''