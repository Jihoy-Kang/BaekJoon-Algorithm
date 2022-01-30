#내 풀이
a = []
b = []
t = 1
n = int(input())
if n <= 9 :
    a.append(0)
    a.append(n)
else :
    a = list(map(int,str(n)))

c = a[0] + a[1]
if c >=10 :
    b = list(map(int, str(c)))
    d = a[1]*10 + b[1]
else :
    d = a[1]*10 + c

while n != d :
    if d < 10 :
        a[0] = 0
        a[1] = d
        c = a[0] + a[1]
    else :
        a = list(map(int,str(d)))
        c = a[0] + a[1]
        
    if c >=10 :
        b = list(map(int, str(c)))
        d = a[1]*10 + b[1]
    else :
        d = a[1]*10 + c

    t += 1

print(t)

#모범답안
n = int(input())
num = n
cnt = 0

while True :
    a = num // 10
    b = num % 10
    c = (a+b)%10
    num = (b*10) + c
    cnt += 1

    if num == n :
        break
print(cnt)