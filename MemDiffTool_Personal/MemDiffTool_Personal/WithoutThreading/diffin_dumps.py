import heatmap_processess as phmap
import heatmap_MemoryDump as memmap
import math
import pandas
import memory_dump as md
import process as pr
import module as mod
import page as pge
import xml_parser as xp

filename_1="Resources/DiffingXml/OhneMalware.xml"
filename_2="Resources/DiffingXml/WithMalware.xml"
   
heatmap_dump_A=xp.parse(md.MemoryDump("heatmap1"),filename_1)
heatmap_dump_B=xp.parse(md.MemoryDump("heatmap2"),filename_2)

