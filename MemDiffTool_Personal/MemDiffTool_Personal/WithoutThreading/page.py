import subprocess
import os
import pandas
import configuration as co
from bisect import *
from pandas import DataFrame
import bisect_module as bi
import time
class Page:
    """
    Page encapsulates the Pages.
    """
    Page_indicator=-100
    def __init__(self, address, print_Ascci,non_print_Ascci,print_Ascci_Num,entropy,size,hash,rlOffset):
        """
        Construct a new 'Page' object.

        :param address: The addresse of the page
        :param print_Ascci: The number of printable Ascii characters
        :param non_print_Ascci: The number of non-printable Ascii characters
        :param print_Ascci_Num: The number of number characters
        :param entropy: The value of the entropy
        :param size: The size of tha page
        :param hash: The hash value of the page binaries
        :param rlOffset: The relative offset between the page and the base module address it related to
        :return: returns nothing
        """
        self.address = address
        self.print_Ascci = print_Ascci
        self.non_print_Ascci = non_print_Ascci
        self.print_Ascci_Num = print_Ascci_Num
        self.entropy = entropy
        self.size=size
        self.hash=hash
        self.rlOffset=rlOffset
