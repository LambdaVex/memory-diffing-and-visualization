import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import bisect_module as bi
import time
class Page:

    def __init__(self, address, print_Ascci,non_print_Ascci,print_Ascci_Num,entropy,size,hash):
        self.address = address
        self.print_Ascci = print_Ascci
        self.non_print_Ascci = non_print_Ascci
        self.print_Ascci_Num = print_Ascci_Num
        self.entropy = entropy
        self.size=size
        self.hash=hash
