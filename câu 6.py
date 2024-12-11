print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
import os

def file_read_from_tail(fname, lines):
    bufsize = 8192 
    fsize = os.stat(fname).st_size  
    iter = 0  
    data = []  

    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize - 1  

        while True:
            iter += 1
            f.seek(fsize - bufsize * iter) 
            chunk = f.readlines()  
            data.extend(chunk)  

            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))
                break

file_read_from_tail('test.txt', 2)
