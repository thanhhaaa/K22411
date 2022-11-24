a = int(input("nhap so a khac 0: "))
b= int(input("nhap so b: "))
c= int(input("nhap so c: "))
s=0
s1=0
s2=0
kq=0
denta= b**2-4*a*c
if (denta>0):
   print ("phuong trinh co hai nghiem")
   kq==kq+1
   s1= -b/(a)
   print ("tong 2 nghiem la:", s1 )
#tim nghiem cua phuong trinh thu nhat: d*X**2+e*X+f=0
d = int(input("nhap so d khac 0"))
e= int(input("nhap so e"))
f= int(input("nhap so f"))
denta= e**2-4*d*f
if (denta>0):
   print ("phuong trinh co hai nghiem")
   kq==kq+2
   s2= -e/(d)
   print ("tong 2 nghiem la:" ,s2 )
if (kq+1) and (kq+2):
   s=s1+s2
   print("tong nghiem 2 phuong trinh la:", s)

