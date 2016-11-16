def read_in_chunks(file_object, chunk_size=1):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield ord(data)

fo = open("forheatmap.txt", "wb")

#put your dump path here ?!
f = open("D:\Dump\A\dump.mem","rb")
line=0
for piece in read_in_chunks(f):
    line=line+1
    if line%16==0:
        fo.write(str(piece)+"\r\n")
    else:
        fo.write(str(piece)+" ")
fo.close()

print("Done")