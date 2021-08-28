import random
mode = int(input('if you want to made a decryption press 1 & enter ; or not press 0 then enter '))
chuoi = str(input('please type your document'))
len_a = len(chuoi)
def khungchuan(chuoi,key):
    sb = str(chuoi[0:key])
    se = str(chuoi[len_a:-1])
    bs = sb[::-1]
    be = se[::-1]
    Q = bs + be
    return Q
if mode == 0:
    key = random.randint(1,len_a)
    Q = khungchuan(chuoi,key)
    print('your text is encrypted , your key is :', key)
    print('you pressed 0 and your text will be explain  ', Q)
elif mode == 1:
    key = int(input('please type your key '))
    Q = khungchuan(chuoi,key)
    print('your text is decryption , your key is :', key)
    print('you pressed 1 and your texxt will be decoded  ', Q)
else:
    print('error')
