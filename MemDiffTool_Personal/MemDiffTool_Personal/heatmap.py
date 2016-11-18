from math import pi

from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper
from bokeh.plotting import figure
from bokeh.sampledata.unemployment1948 import data
from bokeh.charts import HeatMap, output_file, show
from mmapOP import openDumpFile, closeDumpFile




map=openDumpFile("C:\\Users\\ali-d\\Desktop\\Work\\20161029.mem")
print(map[3])
Size=1000
chunk = map.read(Size)
print(type(chunk))
print(len(chunk))

#for i in range(100):
 #   print(chunk[i])
#Mito=[1,23,13,42,6,2,6,48,9,6,5,4,4,5,6,7,28,9,0,4,2,3,4,25,6,7,5,6,8,3,2,3,20,40,30,22,33,44,2,3,1,41,25,23,15,16,17,34,23,63,24,34,34]
#print(type(Mito))
#print(chunk[80])
Tit=[]
for i in range(Size):
    Tit.append(chunk[i])


Mito=[1,23,13,42,6,2,6,48,9,6,5,4,4,5,6,7,28,9,0,4,2,3,4,25,6,7,5,6,8,3,2,3,20,40,30,22,33,44,2,3,1,41,25,23,15,16,17,34,23,63,24,34,34]
print(list(range(9)))
data = {'bytes': ['bytes']*len(Tit)   ,
        'byte_val': Tit,
        'Size': list(range(len(Tit)))}

colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
hm = HeatMap(data, x='bytes', y='Size', values='byte_val',
             title='DataDump', stat=None)
hm.plot_width=800
hm.plot_height=10400

output_file('heatmap.html')
show(hm)


closeDumpFile(map)










'''
from bokeh.charts import HeatMap, output_file, show
from bokeh.palettes import YlOrRd9 as palette
from bokeh.sampledata.unemployment1948 import data

# pandas magic
df = data[data.columns[:-1]]
df2 = df.set_index(df[df.columns[0]].astype(str))
df2.drop(df.columns[0], axis=1, inplace=True)
df3 = df2.transpose()

output_file("cat_heatmap.html")

palette = palette[::-1]  # Reverse the color order so dark red is highest unemployment
hm = HeatMap(df3, title="categorical heatmap", width=800, palette=palette)

show(hm)

'''

'''
data['Year'] = [str(x) for x in data['Year']]

years = list(data['Year'])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data = data.set_index('Year')

# this is the colormap from the original NYTimes plot
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
mapper = LinearColorMapper(palette=colors)
# Set up the data for plotting. We will need to have values for every
# pair of year/month names. Map the rate to a color.
month = []
year = []
color = []
rate = []
for y in years:
    for m in months:
        month.append(m)
        year.append(y)
        monthly_rate = data[m][y]
        rate.append(monthly_rate)

source = ColumnDataSource(
    data=dict(month=month, year=year, rate=rate)
)

TOOLS = "hover,save,pan,box_zoom,wheel_zoom"

p = figure(title="US Unemployment (1948 - 2013)",
           x_range=years, y_range=list(reversed(months)),
           x_axis_location="above", plot_width=900, plot_height=400,
           tools=TOOLS)

p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "5pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

p.rect(x="year", y="month", width=1, height=1,
       source=source,
       fill_color={'field': 'rate', 'transform': mapper},
       line_color=None)

p.select_one(HoverTool).tooltips = [
    ('date', '@month @year'),
    ('rate', '@rate'),
]

show(p)      # show the plot

'''