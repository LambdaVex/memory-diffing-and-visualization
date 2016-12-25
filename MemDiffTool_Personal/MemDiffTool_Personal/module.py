import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame

class Module:

    def __init__(self, name, base,size):
        self.name = name
        self.base = base
        self.size = size
        self.pages = []    

    def add_pages(self,pid):
        print(pid)
        