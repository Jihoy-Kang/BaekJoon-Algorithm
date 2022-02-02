n = list(map(ord, input()))
a = ord('a')
z = ord('z')

for i in range(a,z+1) :
    if i in n :
        print(n.index(i))
    else :
        print(-1)
        
