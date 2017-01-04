import math, string, sys, fileinput

def range_bytes (): return range(256)
def range_printable(): return (ord(c) for c in string.printable)
def H(data, iterator=range_bytes):
    if not data:
        return 0
    entropy = 0
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def entropy_c(data):
    return (H(data, range_printable))



"""
back up
import math, string, sys, fileinput

def entropy_c:


def range_bytes (): return range(256)
def range_printable(): return (ord(c) for c in string.printable)
def H(data, iterator=range_bytes):
    if not data:
        return 0
    entropy = 0
    print("------------------------------------------------------------")
    print("data={0}".format(data))
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        print("p_x={0},x={1}".format(p_x,chr(x)))
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def entropy_c(data):
    for row in fileinput.input():
        string = row.rstrip('\n')
        print("just now i wrote this={0}".format(string))
        print ("%s: %f" % (string, H(string, range_printable)))

for str in ['gargleblaster', 'tripleee', 'magnus', 'lkjasdlk',
               'aaaaaaaa', 'sadfasdfasdf', '7&wS/p(']:
    print ("%s: %f" % (str, H(str, range_printable)))
"""