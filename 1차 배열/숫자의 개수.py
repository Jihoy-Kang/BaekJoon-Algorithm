#내풀이
a = int(input())
b = int(input())
c = int(input())
times = list(map(int, str(a*b*c)))
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0

for i in times[:] :
    if i == 0 :
        c0 += 1
    elif i == 1 :
        c1 += 1
    elif i == 2 :
        c2 += 1
    elif i == 3 :
        c3 += 1
    elif i == 4 :
        c4 += 1
    elif i == 5 :
        c5 += 1
    elif i == 6 :
        c6 += 1
    elif i == 7 :
        c7 += 1
    elif i == 8 :
        c8 += 1
    else :
        c9 += 1

print(c0)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)

#모범답안
a = int(input())
b = int(input())
c = int(input())

result = list(map(int,str(a*b*c)))
print(result)

for i in range(10) :
    print(result.count(int(i)))