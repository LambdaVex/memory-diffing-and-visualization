from math import pi
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.plotting import figure
import pandas as pd
import numpy as NP
import bokeh.palettes as bp
import configuration as co
import time
import memory_dump as md
import page as pg

def display_processheatmap(heatmap_dump):
    
    proc=heatmap_dump.processes[1]

    # define Number of Chunks
    modules=[o.name for o in proc.modules]

   # print(modules[0].hmpages)
    #print("PAUS")
    #time.sleep(6)

    '''
    MODULES=[]
    for i in heatmap_dump.processes:
            MODULES+=i.modules

    modules2=[o.name for o in MODULES]
    print(len(modules2))
   '''

    #T=[o.address for o in proc.modules[1].pages]
    Steps=[]
    for i in range(0,5152):
        Steps.append(str(i))
    #print(len(T))
    #print(len(Steps))
    active=[]
    page = []
    module = []
    value = []
    process=[]
    module_index=0
    step=[]
    modulez=[]
    #modules=[o.name for o in proc.modules]

    '''
    for i in range(1,2):
        for j in heatmap_dump.processes[i].modules:
            for k in Steps:
                step.append(k)
                module.append(j.name)
                modules.append(j.name)
                process.append(heatmap_dump.processes[i].name)
                if(int(k)<len(heatmap_dump.processes[i].modules[module_index].hmpages)):      
                    page.append(heatmap_dump.processes[i].modules[module_index].hmpages[int(k)].address)
                    if(heatmap_dump.processes[i].modules[module_index].hmpages[int(k)].address=="-1"):
                        active.append("-1")
                    else:
                        active.append("1")
                else:
                    page.append("-1")
                    active.append("-1")
            module_index=module_index+1
    ''' 
    #Sum=0   
    #for p in range(1,2):
    #    Sum=Sum+len(heatmap_dump.processes[p].modules)
    #print(len(heatmap_dump.processes))
    #time.sleep(7)
    for p in range(0,5):
        module_index=0
        for m in heatmap_dump.processes[p].modules: # Names of modules
            ind=m.name+"_"+heatmap_dump.processes[p].pid
            modulez.append(ind)
            for y in Steps : # Addresses of pages
                step.append(y)
                module.append(ind)
                process.append(heatmap_dump.processes[p].name)
                if(int(y)<len(heatmap_dump.processes[p].modules[module_index].hmpages)):
                    page.append(heatmap_dump.processes[p].modules[module_index].hmpages[int(y)].address)      
                    if(heatmap_dump.processes[p].modules[module_index].hmpages[int(y)].address=="-1"):
                        active.append("-1")
                    else:
                        active.append("1")
                else:
                    page.append("-1")
                    active.append("-1")
            module_index=module_index+1
    #print(modules)
    modules=modulez

    #print(modulez)
    #time.sleep(7)
    '''
    for m in modules: # Names of modules
        for y in Steps : # Addresses of pages
            step.append(y)
            module.append(m)
            process.append(proc.name)
            if(int(y)<len(proc.modules[module_index].hmpages)):      
                page.append(proc.modules[module_index].hmpages[int(y)].address)
                if(proc.modules[module_index].hmpages[int(y)].address=="-1"):
                    active.append("-1")
                else:
                    active.append("1")
            else:
                page.append("-1")
                active.append("-1")
        module_index=module_index+1
    '''
    source = ColumnDataSource(data=dict(page=page, module=module, process=process,step=step,active=active))
    TOOLS = "hover,save,pan,box_zoom,wheel_zoom"
    #
    # the figure and its properties 
    # 180 for 1,2,3
    # 700 for 10 <Kinda Small>, 900 better
    # 1400 for 0 -> 13
    p = figure(title="Memory Info",
               x_range=Steps, y_range=list(reversed(modules)),
               x_axis_location="above", plot_width=20000, plot_height=1500,
               tools=TOOLS,toolbar_location="above")

    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = pi / 3
       
    #colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    colors = ["#ffffff", "#000000"]
    mapper = LinearColorMapper(palette=colors)

    # modifying every rectangle
    p.rect(x="step", y="module", width=1, height=1,
           source=source,
           # fill_color={'field': 'value', 'transform': mapper},
           fill_color={'field': 'active', 'transform': mapper},
           line_color='white')

    # info to display on hover
    p.select_one(HoverTool).tooltips = [
        ('info', '@module'),
        ('page', '@page'), 
        ('active', '@active'), 
        ('process', '@process'), 
    ]
    p.xaxis.visible = False
    show(p)      # show the plot










    '''
     for m in modules: # Names of modules
        
        #print("Now: "+str(m))
        #print(module_index)

        for y in Steps : # Addresses of pages
            step.append(y)
            module.append(m)
            process.append(proc.name)
           # page.append(proc.modules[1].pages[int(y)].address)
            if(int(y)<len(proc.modules[module_index].hmpages)):
                #print("append: "+str(proc.modules[module_index].hmpages[int(y)].address))
                page.append(proc.modules[module_index].hmpages[int(y)].address)
                if(proc.modules[module_index].hmpages[int(y)].address=="-1"):
                    active.append("-1")
                else:
                    active.append("1")
                
                #value.append(y)
            else:
                #print("append: -1")
                page.append("-1")
                active.append("-1")
        module_index=module_index+1
    '''