'''a='01012345678'
b=('*'(len(a)-4))+(a[-4:])
print(b)



l=[5,9,7,10]
e=[]
d=5

for i in l:
    if i%d==0:
        e.append(i)
if len(l)==0:
    e.append('-1')
else:
    e.sort()
print(e)



num=16
c=0
while c<500:
    if num%2==0:
        num/=2
    else:
        num=num*3+1
    c+=1
    if num==1:
        break
if num==1:
    print(c)
else:
    print('-1')'''



s=str(input('write any number:'))
c=0
for i in s:
    if i=='1':
        c+=1
print(c)