import mmap
import threading
import time

choose=dict()
count=1
choice=0

class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        file_name="{}.txt".format(self.getName())
        #drawing the heatmap
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

with open("D:\\Dump\\A\\dump.mem", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print("Choices available:")
    size=mm.size()
    factors=factors(size)
    for i in factors:
        print '{ch}_)The number of chunks:{c} and each one size is:{cc}'.format(ch=count,c=size/i,cc=i )
        choose[count]=i
        count=count+1
    choice = input("write the number of your choice: ")
    bytes=choose[choice]
    for i in range(size/bytes):
        fo = open('{name}.txt'.format(name=i), "wb")
        fo.write(mm.read(bytes))
        fo.close()
        #mythread = MyThread(name = "Thread-{}".format(i))
        #mythread.start()
    # close the map
    mm.close()


