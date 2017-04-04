import os
def textual_compare(first_file,second_file):
    """
    Initiate the textual representation
    """
    os.system('diff2HtmlCompare.py -s '+first_file+' '+second_file)
