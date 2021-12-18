try:
    dic=dict.fromkeys(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M','N','O','P','Q','R','S','T','U','V',
         'W','X','Y','Z'],0)
    cnt = 0
    inp = open('test.txt', "rt")
    content = s.read()
    for ch in content:
       ch=ch.upper()
       cnt += 1
       if ch in dic:
           dic[ch]+=1
 
    print("\n\nCharacters in file:", cnt)
    for x,y in dic.items():
        print("{}: {}".format(x,y))
        
    inp.close()
    
except IOError:
    print("I/O error occurred ")
