#coding=utf-8
# for i in range(4,0,-1):#i表示空格数量
#     print(' '*(i-1),'*'*(2*(5-i)-1))   #(2*(5-i)-1)表示行号

for i in range(4,0,-1):
    print(' '*(i-1)),
    for j in range(1,5,1):#j表示行号
        print('*'*(2*j-1))