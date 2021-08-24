n = str(input(' nhập vào 1 chuỗi '))
m =  list(n)
c = len(m)
d = int(c/2)
cut_1 = m[0:d]
cut_2 = m[d:]

if n == n[::-1]:
    print("Chuỗi đối xứng")
elif c%2 == 0 and cut_2 == cut_1 :
    print('Chuổi này cũng là chuỗi đối xứng ')
else:
    print("Chuỗi không đối xứng")