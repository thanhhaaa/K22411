s=0
thu=0
for i in range (1,3):
   a = int(input("nhap so a: "))
   b = int(input("nhap so b: "))
   c = int(input("nhap so c: "))
   while (a==0):
       a=int(input('vui lòng nhập lại số a: '))
   else:
       denta= b**2-4*a*c
       if (denta>0):
           kq=1
           s1=-b/a
       else:
           kq=0
           s1=0
       print (s1)
       thu=thu+kq
   if kq == 1 :
      s=s+s1
if thu == 2:
      print("tong nghiem cua 2 phuong trinh khi co 2 nghiem la:", s)
else:
    print('2 phương trình không thỏa điều kiện cần')

