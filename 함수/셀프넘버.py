#내 풀이
d = []
for i in range(1,10001) :
    a = list(map(int, str(i)))
    for j in a :
        i += j
    d.append(i)

for i in range(1,10001) :
    if i not in d :
        print(i)

#모범답안
natural_num = set(range(1,10001)) # 1부터 10000까지 집합
generated_num = set() #생성자가 있는 숫자 집합 선언

for i in range(1,10001) :
    for j in str(i) :
        i += int(j)
    generated_num.add(i) #집합 추가함수 add

self_num = sorted(natural_num-generated_num) #1부터 10000까지 숫자중 생성자가있는 숫자집합의 차집합
for i in self_num :
    print(i)


