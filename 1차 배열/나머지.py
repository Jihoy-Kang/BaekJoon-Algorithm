list = []
result = []
resulta = []
for i in range(10) :
    list.append(int(input()))

for i in range(10) :
    result.append(int(list[i]%42))

for i in result :
    if i not in resulta :
        resulta.append(i)
    
print(len(resulta))