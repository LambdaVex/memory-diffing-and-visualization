from math import pi
from bokeh.io import output_file, show, vplot, gridplot, hplot
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.plotting import figure
import pandas as pd
import numpy as NP
import bokeh.palettes as bp
import configuration as co
import time
import memory_dump as md
import page as pg
import toolz as tz
import memory_dump as md
import process as pr
import module as mod
import page as pge

def display_diffingheatmap(heatmap_dump):
    
    list_modules=[]
    
    for proc in heatmap_dump.processes:
        for module in proc.modules:
            module.name=module.name.lower()
           
    #Omit the first one
    for proc in heatmap_dump.processes:
        for module in range(1,len(proc.modules)):
            list_modules.append(proc.modules[module])
    
    list_modules.sort(key = lambda x: x.base)
    list_modules=list(tz.unique(list_modules, key=lambda x: x.name))
    ListOfobsoletePages= [[] for i in range(len(list_modules))]


    heatmap_dump.processes=list(tz.unique(heatmap_dump.processes, key=lambda x: x.pid))

    for proc in heatmap_dump.processes:
        if(proc.P_indicator==-100):
            proc.summodules=[0]*len(list_modules)
        if(proc.P_indicator==-1):
            proc.summodules=[-30]*len(list_modules)
        if(proc.P_indicator==1):
            proc.summodules=[30]*len(list_modules)

    '''
        for mod in pr.modules:
           #print(mod.name)
           index=get_index(list_modules,mod.name)
           if(index!=-1):
               # How many pages percent %
               pr.summodules[index]= sum(int(c.size,0) for c in mod.pages)/int(mod.size,0) 
               #ListOfPages[index].extend(mod.pages)
               ListOfobsoletePages[index].extend(mod.pages)
               #print(str(pr.summodules[index])+" len: "+str(len(str(pr.summodules[index]))) )
               if(len(str(pr.summodules[index]))>4):
                   pr.summodules[index]=float(str(pr.summodules[index])[:6])*100
    '''
    #for i in range(0,len(ListOfobsoletePages)):
    #    ListOfobsoletePages[i]=list(tz.unique(ListOfobsoletePages[i], key=lambda x: x.rlOffset))
    '''
    SummaryList=[0]*len(list_modules)
    for i in range(0,len(list_modules)):
        if(len(ListOfobsoletePages[i])!=0):
            #print(i)
            xval= (((max(int(node.rlOffset,0) for node in ListOfobsoletePages[i]))/4096)+1)
            yval=(len(ListOfobsoletePages[i]))

            SummaryList[i]=int(yval*100/xval)

    print(SummaryList[20])
    print(list_modules[20].name)
    '''









    print("RIGHT DIRRECT")
    #time.sleep(5)
    # define processes on Y-Axis
    processes=[o.name+" / "+o.pid for o in heatmap_dump.processes]
    # define modules on X-Axis
    Steps=[o.name for o in list_modules]
    listP=[]*len(list_modules)
    #Summary_List=[0]*len(listM)
    modulelist = []
    process=[]
    module_index=0
    step=[]
    process_val=[]
    base_address=[]
    for proc in heatmap_dump.processes: # Names of processes
        #print(module_index)
        #print("now"+proc.name)
        module_index=0
        for module in list_modules : # Addresses of modules
            step.append(module.name)
            base_address.append(module.base)
            process.append(proc.name+" / "+proc.pid)
            #Summary_List[module_index]=Summary_List[module_index]+proc.summodules[module_index]
            modulelist.append(proc.summodules[0])
            process_val.append(proc.summodules[0])
          
            module_index=module_index+1
    time.sleep(10)
    source = ColumnDataSource(data=dict(modulelist=modulelist, process=process,step=step,base_address=base_address,process_val=process_val))
    TOOLS = "hover,save,pan,box_zoom,wheel_zoom"
    # the figure and its properties 
    p = figure(title="Memory Dump Visualization",
               x_range=Steps, y_range=list(reversed(processes)),
               #x_axis_location="above", plot_width=1450, plot_height=700,
               x_axis_location="above", plot_width=1450, plot_height=850,
               tools=TOOLS,toolbar_location="above")
    p.border_fill_color = "whitesmoke"
    p.min_border_bottom = 10
    #p.min_border_right = 10
    p.toolbar.logo = None
    #p.toolbar_location = None
    #p.logo=None
    #p.toolbar_location = None

    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = pi / 3
       
    #colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    colors = ["#ff0000", "#FFD000", "#FFD000","#2B8318"]
    
    mapper = LinearColorMapper(palette=colors)

    # modifying every rectangle
    p.rect(x="step", y="process", width=1, height=1,
           source=source,
           # fill_color={'field': 'value', 'transform': mapper},
           fill_color={'field': 'process_val', 'transform': mapper},
           line_color='white')

    # info to display on hover
    p.select_one(HoverTool).tooltips = [
        ('Process / PID', '@process'),
        ('Module', '@step'),
        ('Value', '@process_val'),
    ]
    p.xaxis.visible = False
    p.yaxis.visible = False

  
   
    output=vplot(p)
    show(output)      # show the plot
