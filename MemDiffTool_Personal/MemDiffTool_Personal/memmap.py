from bokeh.charts import Histogram, output_file, show
from bokeh.layouts import row
from bokeh.sampledata.autompg import autompg as df
import pandas as pd
import numpy as np

list=[1,2,3,4,5,6,7,8,9]
print(list)
list2=list[1:]
print(list2)



data = {
    'sample': ['1st', '2nd', '1st', '2nd', '1st', '2nd'],
    'interpreter': ['python', 'python', 'pypy', 'pypy', 'jython', 'jython'],
    'timing': [-2, 5, 12, 40, 22, 30]
}
print(data)



'''
tips = pd.read_csv("C:\\Users\\ali-d\\Desktop\\Work\\csv\\bytes2.csv")
#arr=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8]
hist = Histogram(tips, values='mpg',bins=40, title="Auto MPG Histogram", plot_width=900)


output_file('hist.html')
show(row(hist))

'''