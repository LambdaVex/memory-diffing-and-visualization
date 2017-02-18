import mmap
import numpy as NP
from bokeh.charts import Histogram,Bar, output_file, show
from bokeh.layouts import row
from bokeh.sampledata.autompg import autompg as df
import pandas as pa



column_of_values = NP.memmap("D:\\visual studio 2015\\Projects\\HeatProducerWithAli\\MemDiffTool_Personal\\MemDiffTool_Personal\\1.txt")

bins = NP.array(range(0,256))
binned_values = NP.digitize(column_of_values, bins)
temp=NP.bincount(binned_values)

data={
    'values':bins,
    'occurence':temp[1:]
    }

# x-axis labels pulled from the interpreter column, stacking labels from sample column
bar = Bar(data, values='occurence', label='values',
          title="Python Interpreter Sampling",  plot_width=4000)

output_file("stacked_bar.html")
show(row(bar))