n = int(input())
for i in range(n) :
    r, s = input().split()
    r = int(r)
    s = list(str(s))
    P = str()
    for i in s :
        P += (i*r)
    print(P)