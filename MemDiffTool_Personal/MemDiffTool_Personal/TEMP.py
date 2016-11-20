from bokeh.charts import HeatMap, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper, ColumnDataSource
import pandas as pd
import numpy as np
#matrix = numpy.matrix([[1, 2],[3, 4]])

# (dict, OrderedDict, lists, arrays and DataFrames are valid inputs)
#data = {'fruit': ['apples']*5 ,
#        'fruit_count': [10,2,3,4,5],
#        'sample': [1,2,3,4,5]}

tips = pd.read_csv("C:\\Users\\ali-d\\Desktop\\Work\\fruit.csv")
info=ColumnDataSource(tips)
print(info)
#info=ColumnDataSource(tips[tips["letter"]])
#print(data)
#s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
#data2 = [1,2,3,4,5,6,7,8]
hm = HeatMap(tips, x='fruit', y='sample', values='fruit_count',
            title='Fruits', stat=None)
#hm = HeatMap(s,x='x', y='y')
hover=HoverTool(tooltips=[("Num","@letter")])
hm.add_tools(hover)

hm.select_one(HoverTool).tooltips = [
    ('Num', '@letter')]

output_file('heatmap.html')
show(hm)