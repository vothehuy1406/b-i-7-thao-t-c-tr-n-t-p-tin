print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
def file_read(fname):
    
    with open(fname, "a") as myfile:
        # Nối văn bản vào tệp
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    
    with open(fname, "r") as myfile:
        # Đọc và hiển thị toàn bộ nội dung tệp
        print(myfile.read())

# Gọi hàm để thực hiện chức năng
file_read('xyz.txt')
