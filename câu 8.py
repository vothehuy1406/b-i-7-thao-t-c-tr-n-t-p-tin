def write_list_to_file(filename, data_list):
    try:
        
        with open(filename, 'a', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")  
        
      
        print(f"Nội dung đã được ghi vào tệp '{filename}'.")
        
        # Đọc và in nội dung trong tệp sau khi ghi
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\nNội dung trong tệp:")
            print(content)  

    except Exception as e:
        print(f"Có lỗi xảy ra khi ghi vào tệp: {e}")

def main():
   
    filename = input("Nhập tên tệp (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    
   
    data_list = ['anh', 'yeu', 'em', 'nhieu', 'lam']
    
    
    write_list_to_file(filename, data_list)

if __name__ == "__main__":
    main()
