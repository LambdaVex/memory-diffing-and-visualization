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
def diffProcesses(Proc_A,Proc_B):
    base_listA = {module.base for module in Proc_A.modules}
    for module in Proc_B.modules:
        if module.base not in base_listA:
            #print (process.pid )
            module.M_indicator=1
            #dump_Diff.processes.append(process)

    #print("Deleted Processes")
    base_listB = {module.base for module in Proc_B.modules}
    for module in Proc_A.modules:
        if module.base not in base_listB:
            #print (process.pid )
            module.M_indicator=-1
            #dump_Diff.processes.append(process)

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




filename_1="Resources/DiffingXml/WithoutMalware.xml"
filename_2="Resources/DiffingXml/WithMalware.xml"
   
dump_A=xp.parse(md.MemoryDump("heatmap1"),filename_1)
dump_B=xp.parse(md.MemoryDump("heatmap2"),filename_2)

dump_Diff = md.MemoryDump("DIFF")
#for i in heatmap_dump_B.processes:
#    print (i.pid)

#dump_A.processes[0].P_indicator=1
#print("New Processes")
pid_listA = {process.pid for process in dump_A.processes}
for process in dump_B.processes:
    if process.pid not in pid_listA:
        #print (process.pid )
        process.P_indicator=1
        dump_Diff.processes.append(process)

#print("Deleted Processes")
pid_listB = {process.pid for process in dump_B.processes}
for process in dump_A.processes:
    if process.pid not in pid_listB:
        #print (process.pid )
        process.P_indicator=-1
        dump_Diff.processes.append(process)


for i in dump_A.processes:
    if(i.P_indicator==-100):
        dump_Diff.processes.append(i)
for i in dump_B.processes:
    if(i.P_indicator==-100):
        dump_Diff.processes.append(i)




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


hmapdiff.display_diffingheatmap(dump_Diff,dump_A,dump_B)
print("Done")