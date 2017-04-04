import math, string, sys, fileinput

def entropy_c(data):
    """
    Calculate the entropy of a chunk of memory
    """
    b_data = bytearray(data)
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(b_data.count(x))/float(len(b_data))
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy