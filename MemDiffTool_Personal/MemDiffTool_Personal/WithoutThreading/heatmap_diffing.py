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

def get_index(list_modules,module):
    for index, item in enumerate(list_modules):
        if item.name == module:
            break
        else:
            index = -1
    return index

def diff_modules(mod_A,mod_B):
    """
    Diff two different modules 
    """  
    flag=3    # blue

    
    for i in mod_B.pages:
        for j in mod_A.pages:
            if(i.rlOffset==j.rlOffset):
                if(i.hash==j.hash):
                    flag=3 # Blue
                elif(i.hash!=j.hash):
                    return 2 # bright red
    for i in mod_A.pages:
        for j in mod_B.pages:
            if(i.rlOffset==j.rlOffset):
                if(i.hash==j.hash):
                    flag=3 # Blue
                elif (i.hash!=j.hash):
                    return 2 # bright red
    return flag
#3,4,5
def diff_processes(proc_A,proc_B):
    """Create a list of modules in Proc_A. (New Modules)
    If a module in Proc_B doesn't appear in Proc_A, then assign the tag 1 (New)
    The process is repeated for modules in Proc_B
    Finally for processes that have the default value, we do some more processing on the page level
    """
    base_listA = {module.base for module in proc_A.modules}
    Temp=[]
    for module in proc_B.modules:
        if module.base not in base_listA:
            module.M_indicator=5     #bright green
            Temp.append(module)

    # Delete Modules
    base_listB = {module.base for module in proc_B.modules}
    for module in proc_A.modules:
        if module.base not in base_listB:
            module.M_indicator=6     #black  
            Temp.append(module)

    for i in proc_A.modules:
        if(i.M_indicator==-100):
            #print("1.2. going to diff: "+i.base)
            stats=diff_modules(i,next((x for x in proc_B.modules if x.base == i.base), None))
            i.M_indicator=stats
            Temp.append(i)
    return Temp


def display_diffingheatmap(heatmap_dump,dump_A,dump_B):
    """
    Process and display the diffing heatmap
    """  
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

    #because data coming from two dumps
    heatmap_dump.processes=list(tz.unique(heatmap_dump.processes, key=lambda x: x.pid))

    #for i in list_modules:
    #    print(i.name)
    #print("_-----------------------")

    for proc in heatmap_dump.processes:
        #old
        if(proc.P_indicator==-100):
            #print("1. going to diff: "+proc.pid)
            proc.summodules=[7]*len(list_modules)
            Nmodules=[]
            Nmodules=diff_processes(next((x for x in dump_A.processes if x.pid == proc.pid), None),next((x for x in dump_B.processes if x.pid == proc.pid), None))
            for modl in Nmodules:
                index=get_index(list_modules,modl.name)
                #if(index==-1):
                #    print("WARNING "+modl.name)
                if(index!=-1):
                    proc.summodules[index]= modl.M_indicator
            #print(proc_A.pid,proc_B.pid)
            
        #disappear
        if(proc.P_indicator==-1):
            proc.summodules=[1]*len(list_modules)
        #new
        if(proc.P_indicator==1):
            proc.summodules=[4]*len(list_modules)
            for mod in proc.modules:
                index=get_index(list_modules,mod.name)
                if(index!=-1):
                    proc.summodules[index]= 5


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
            modulelist.append(proc.summodules[module_index])
            process_val.append(proc.summodules[module_index])
          
            module_index=module_index+1
    #time.sleep(10)
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
    
    # blue #0000ff black #000000
    # 1 red, 2 bright red, 3 blue, 4 dark green, 5 bright green, 6 black , 7 grey
    colors = ["#ff0000", "#0000ff","#A3C795","#03FF23","#000000", "#D3D3D3"]
    
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







