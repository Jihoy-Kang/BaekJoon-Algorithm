#내 풀이
a,b = map(list, input().split())
c = []
d = []
for i in a :
    c = list(i) + c

for i in b :
    d = list(i) + d

a = str()
b = str()

for i in c :
    a += i

for i in d :
    b += i

if int(a) > int(b):
    print(a)
else :
    print(b)
