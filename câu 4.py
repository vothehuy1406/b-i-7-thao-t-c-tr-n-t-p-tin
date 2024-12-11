print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
from itertools import islice
def file_read_from_head(fname, nlines):
    with open(fname, 'r') as f:
        for line in islice(f, nlines):
            print(line, end='') # Gọi hàm với tệp 'test.txt' và số dòng cần đọc
file_read_from_head('test.txt', 2)
