print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
import re

def find_longest_words(text):
     
    words = re.findall(r'\b\w+\b', text)
    
    
    max_length = max(len(word) for word in words)
    
   
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words, max_length

def main():
    
    text = input("Nhập văn bản để tìm từ dài nhất: ")
    
   
    longest_words, max_length = find_longest_words(text)
    
   
    print(f"Các từ dài nhất (có độ dài {max_length} ký tự):")
    for word in longest_words:
        print(word)

if __name__ == "__main__":
    main()
