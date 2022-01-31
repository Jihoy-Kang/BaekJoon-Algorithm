n = int(input())

for i in range(n) :
    ox = list(map(str, input()))
    result = 0
    cnt = 0
    for j in range(len(ox)) :
        if ox[j] == 'O' :
            cnt += 1
            result += cnt

        else :
            cnt = 0
    print(result)