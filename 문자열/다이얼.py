a = list(map(ord,input()))
sec = 0
total = 0

for i in a :
    if int(i) <= 79 :
        sec = (int(i)-56)//3
        total += sec
    elif int(i) <= 83 :
        sec = 8
        total += sec
    elif int(i) <= 86:
        sec = 9
        total += sec
    else :
        sec = 10
        total += sec
print(total)