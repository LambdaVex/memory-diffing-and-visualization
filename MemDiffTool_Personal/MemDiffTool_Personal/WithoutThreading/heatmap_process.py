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


def display_processheatmap(proc):
    """
    Build and show the memory heatmap of a process
    """
    # define Number of Chunks
    modules=[o.name for o in proc.modules]

    for i in proc.modules:
        Val_New=[]
        for j in range(len(i.pages)):
            if(j+1!=len(i.pages)):
                Val_New.append(i.pages[j])
                distance=(int((int(i.pages[j+1].address,16)-int(i.pages[j].address,16))/4096))
                Val_New=Val_New+[pg.Page("-1","-1","-1","-1")]*((int(distance))-1)
        Val_New.append(i.pages[len(i.pages)-1])
        i.pages=Val_New

    T=[o.address for o in proc.modules[1].pages]
    Steps=[]
    for i in range(0,len(T)):
        Steps.append(str(i))
    #print(len(T))
    #print(len(Steps))
    page = []
    module = []
    value = []
    process=[]
    module_index=0
    step=[]
    for m in modules: # Names of modules
        #print(module_index)
        for y in Steps : # Addresses of pages
            step.append(y)
            module.append(m)
            process.append(proc.name)
           # page.append(proc.modules[1].pages[int(y)].address)
            
            if(int(y)<len(proc.modules[module_index].pages)):
                page.append(proc.modules[module_index].pages[int(y)].address)
                #value.append(y)
            else:
                page.append("-1")
                
                #index+=1
                #print(y)
            #

        module_index=+1
    #print(Steps)
    #print("PAUS")
    #print(proc.modules[1].pages[len(proc.modules[1].pages)-1].address)
    time.sleep(5)
    source = ColumnDataSource(data=dict(page=page, module=module, process=process,step=step))
    TOOLS = "hover,save,pan,box_zoom,wheel_zoom"
    #
    # the figure and its properties 
    p = figure(title="MemDmp",
               x_range=Steps, y_range=list(reversed(modules)),
               x_axis_location="above", plot_width=1400, plot_height=200,
               tools=TOOLS)

    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = pi / 3
       
    colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    mapper = LinearColorMapper(palette=colors)

    # modifying every rectangle
    p.rect(x="step", y="module", width=1, height=1,
           source=source,
           # fill_color={'field': 'value', 'transform': mapper},
           fill_color={'field': 'page', 'transform': mapper},
           line_color='white')

    # info to display on hover
    p.select_one(HoverTool).tooltips = [
        ('info', '@module'),
        ('page', '@page'), 
        ('process', '@process'), 
    ]
    #p.xaxis.visible = False
    show(p)      # show the plot
