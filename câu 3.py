print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
try:
    with open('D:/vohuy.txt', 'r') as file:  
        content = file.read() 
        print(content) 
except FileNotFoundError:
    print("Tệp không tồn tại. Hãy kiểm tra lại đường dẫn.")
