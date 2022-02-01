#내 풀이 1차
n = int(input())

if n >= 100 :
    cnt = 99
    for j in range(100,n+1):
        a = list(map(int, str(j)))
        s = set()
        for i in range(len(a)-1) :
            s.add(a[i] - a[i+1])
        if len(s) == 1 :
            cnt += 1
else :
    cnt = n
            
print(cnt)

#내 풀이 2차
n = int(input())
cnt = 0
for j in range(1,n+1):
    a = list(map(int, str(j)))
    s = set()
    for i in range(len(a)-1) :
        s.add(a[i] - a[i+1])
        
    if len(s) == 1 or len(s) == 0 :
        cnt += 1
print(cnt)
            
