import tkinter
import pandas
import os
from tkinter.filedialog import askopenfilename

# Method that provide browing capability
def browse():
    global infile
    infile=askopenfilename()
    return infile

# Read the process tree and operate on the memory layout 
def processMemory():
    df3=pandas.read_fwf(infile)
    for i in range(len(df3)):   
        if(df3.iloc[i,0][0]=='0'):
            #print(df3.iloc[i,0][0])
            hexVal=df3.iloc[i,0][2:]
            decVal=int(hexVal, 16)
            bitVal=bin(decVal)
           # print("{0}".format(bitVal))
            print("{0} --> {1} --> {2}".format(df3.iloc[i,0],decVal,bitVal))




# Gui Creation    

gui = tkinter.Tk()
gui.geometry("500x100")
gui.title("MemoryDiff")

label=tkinter.Label(gui,text="Extract Dump")
label.pack()
browseButton=tkinter.Button(gui,text="Browse",command=browse)
browseButton.pack()
processButton=tkinter.Button(gui,text="Process",command=processMemory)
processButton.pack()

x=18446738026422931552
#print(x)
#print(bin(x))

gui.mainloop()