a = []
for i in range(9) :
    a.append(int(input()))

max = max(a)
cnt = 1
    
for i in range(9) :
    if int(a[i]) != max :
        cnt += 1
    else :
        break
    
print(max)
print(cnt)