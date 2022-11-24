n = int(input('n='))
s = 0
for i in range(1, n+1):
 a = float(input('nhap so a: '))
 b = float(input('nhap so b: '))
 c = float(input('nhap so c: '))
 dt = b*b - 4*a*c
 if dt == 0:
  x = -(b/(2*a))
  s = s+x
print('tong nghiem la ', s)