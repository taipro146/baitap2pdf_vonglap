n =  int(input('nhập n từ bàn phím '))
def soam():
     if n <= 0 :
        print(' số âm ')
        return False
def soduong():
    m = float(n/4096)
    if m <= 1 :
        m1 = 1
    else :
        m1 = int(m+0.9999999)
    print(m1)
    t = 4*m1
    k = str(t) + ' KB' # số lần KB

    if m <= 1 and n <= 4096:
        print('file cần bô nhớ là ',k)
    elif m > 1 and n > 4096:
        print('file cần bộ nhớ là ', k)


soduong()
