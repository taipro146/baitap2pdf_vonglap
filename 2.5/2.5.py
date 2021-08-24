
from collections import Counter
n = str(input('nhập chuỗi '))
list_1 = list(n)                    # chuyển n thành list
cont_1 = Counter(list_1)            # tạo biết đêm
t = list_1[0]                       # kí tự đầu tiên
nums = cont_1[t]
c = len(list_1)
print('chuỗi bao gồm  ',c)
a = int(c/nums)
print('')
print('số lần lặp lại của tù đầu tiên là ',nums)
cut_1 = list_1[:a]
cut_2 = list_1[(c-a):(c+1)]
for i in range(0,(c-a-1),1):
    if list_1[i] != list_1[i+a]:
        print('không phải CHUỔI lặp ')
        break
    elif list_1[i] == list_1[i+a] and list_1[:a] == list_1[(c-a):(c+1)] :
        print('là chuổi lặp ')
        break
    else :
        print('unknow - ko phải chuỗi lặp ')
        break