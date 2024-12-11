print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
def copy_file_content(source_file, destination_file):
    try:
        
        with open(source_file, 'r', encoding='utf-8') as source:
            
            content = source.read()

        
        with open(destination_file, 'w', encoding='utf-8') as destination:
           
            destination.write(content)

        print(f"Nội dung từ tệp '{source_file}' đã được sao chép sang tệp '{destination_file}'.")

      
        with open(destination_file, 'r', encoding='utf-8') as destination:
            copied_content = destination.read()
            print("\nNội dung trong tệp đích:")
            print(copied_content) 
    
    except FileNotFoundError:
        print(f"Tệp nguồn '{source_file}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
   
    source_file = "sothutu.txt"
    destination_file = "notepaddich.txt"

   
    copy_file_content(source_file, destination_file)

if __name__ == "__main__":
    main()
