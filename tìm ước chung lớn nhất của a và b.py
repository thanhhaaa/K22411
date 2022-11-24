#tìm ước chung lớn nhất của hai số a b
a=int(input('nhập số a: '))
b=int(input('nhập số b: '))
for i in range (1,a +1):
    if a%i==0:
        uoca=i
        #print('ước của a là: ',uoca)
    for j in range (1,b +1):
        if b%j==0:
            uocb=j
            #print('ước của b là: ',uocb)
            if uoca==uocb:
                uocchung=uocb
                print('ước chung của a và b là: ',uocchung)
print('ước chung lớn nhất của a và b là: ',uocchung)
