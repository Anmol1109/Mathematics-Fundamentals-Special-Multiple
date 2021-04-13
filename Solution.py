import sys

T = int(raw_input())

for i in range(T):
        x = int(raw_input())
        flag = 1
        num = [9]
        temp = []
        while (flag == 1):
                for i in num:
                    if (i%x == 0):
                        print(i)
                        flag = 0
                        break;                    
                    else:
                        temp.append(i*10)
                        temp.append(i*10+9)    
                num = temp
                temp = []
    
