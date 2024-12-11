print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
def read_and_reverse_file(filename):
    try:
        
        with open(filename, 'r') as file:
            
            content = file.readlines()
        
        
        reversed_content = content[::-1]
        
        
        for line in reversed_content:
            print(line.strip())  

    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    filename = input("Nhập tên file (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    read_and_reverse_file(filename)

if __name__ == "__main__":
    main()
