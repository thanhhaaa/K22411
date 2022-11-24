n=int(input('n= '))
s1=1
s2=1
s3=2
for i in range (n-3):
    s1=s2
    s2=s3
    s3=s1+s2
if n>2:
    print(s3)
else:
    print(1)

