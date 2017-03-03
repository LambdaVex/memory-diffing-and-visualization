from math import pi
from bokeh.io import output_file, show, vplot
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.plotting import figure
import pandas as pd
import numpy as NP
import bokeh.palettes as bp
import configuration as co
import time
import memory_dump as md
import page as pg

def display_summaryhp(dumpM,listM,SummaryList):
    #print(Summary_List)
    time.sleep(5)
    # define processes on Y-Axis
    processes=["Summary"]
    # define modules on X-Axis
    Steps=[o.name for o in listM]

    module = []
    process=[]
    module_index=0
    step=[]
    process_val=[]
    base_address=[]
    for proc in processes: # Names of processes
        #print(module_index)
        #print("now"+proc.name)
        module_index=0
        for mod in listM : # Addresses of modules
            step.append(mod.name)
            base_address.append(mod.base)
            process.append(proc)
            if(SummaryList[module_index]==0):
                module.append(-30)
                process_val.append(0)
            else:
                module.append(SummaryList[module_index])
                process_val.append(SummaryList[module_index])
            #process_val.append(1)
            '''
            if(proc.summodules[module_index]==0):
                module.append(-100)
                process_val.append(0)
            else:
                module.append(proc.summodules[module_index])
                process_val.append(proc.summodules[module_index]/10)#normalization
            '''
            module_index=module_index+1
       #CHECK HERE
    print(process_val[248])
    print("VAL")
    print(SummaryList[248])

    #time.sleep(5)
    source = ColumnDataSource(data=dict(module=module, process=process,step=step,base_address=base_address,process_val=process_val))
    TOOLS = "hover,save,pan,box_zoom,wheel_zoom"
    # the figure and its properties 
    p = figure(title="Summary",
               x_range=Steps, y_range=list(reversed(processes)),
               x_axis_location="above", plot_width=1450, plot_height=50,
               tools=TOOLS,toolbar_location="below")
    #p.border_fill_color = "whitesmoke"
    #p.min_border_left = 80
    #p.min_border_bottom = 10
    #p.min_border_right = 10
    #p.min_border_top = 10
    p.toolbar.logo = None
    p.toolbar_location = None


    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = pi / 3
       
    #colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    colors = ["#f2f2f2", "#990000","#e59400","#e5e500","#007300","#0000e5"]     
    mapper = LinearColorMapper(palette=colors)

    # modifying every rectangle
    p.rect(x="step", y="process", width=1, height=1,
           source=source,
           # fill_color={'field': 'value', 'transform': mapper},
           fill_color={'field': 'module', 'transform': mapper},
           line_color='white')

    # info to display on hover
    p.select_one(HoverTool).tooltips = [
      #  ('Process / PID', '@process'),
        ('Module', '@step'),
        ('Address', '@base_address'),  
        ('Value', '@process_val'),
    ]
    p.xaxis.visible = False
    p.yaxis.visible = False

    return(p)
    #output=vplot(p)
    #show(output)      # show the plot
