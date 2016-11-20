import pandas as pd
from bokeh.charts import HeatMap
from bokeh.plotting import output_file, show
from bokeh.models import HoverTool

#tips = pd.read_csv('https://raw.githubusercontent.com/pydata/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv("C:\\Users\\ali-d\\Desktop\\Work\\tips.csv")
hm = HeatMap(tips, x='total_bill', y='id',  values='total_bill',  tools='hover')
output_file("heatmap-tooltip.html", title="heatmap-tooltip")
show(hm)

