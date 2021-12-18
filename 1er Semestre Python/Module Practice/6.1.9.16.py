continuar = 1
while continuar:
    try:
        dic = dict.fromkeys(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                             'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 0)
        cnt = 0
        file = input("Input the name of the file: ")
        inp = open(file, "rt")
        content = inp.read()
        for ch in content:
           ch = ch.upper()
           cnt += 1
           if ch in dic:
               dic[ch]+=1

        print("\n\nCharacters in file:", cnt)
        newDic = sorted(dic.items(), key=lambda elem: elem[1], reverse=True)
        for i in range(len(newDic)):
            print(newDic[i])
        inp.close()

    except IOError:
        print("I/O error occurred ")

    continuar = int(input("Want to continue? (Yes - 1 | No - 0) "))
