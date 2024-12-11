print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
with open('D:/vohuy.txt', 'r') as file:
    char = 0  
    wc = 0     
    lc = 0
    
    for line in file:
        lc += 1 
        char += len(line)  
        
        words = line.split()
        wc += len(words)
        
  
    print("The no. of chars is %d" % char)
    print("The no. of words is %d" % wc)
    print("The no. of lines is %d" % lc)
