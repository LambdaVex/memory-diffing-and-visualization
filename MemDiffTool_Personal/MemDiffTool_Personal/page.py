import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import bisect_module as bi
import time
class Page:

    def __init__(self, name, base,size):
        self.name = name
        self.base = base
        self.size = size
     