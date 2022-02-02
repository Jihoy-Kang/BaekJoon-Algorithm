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
n = int(input()) # 입력값(N)
cnt = 0 # 출력값 넣을 변수
for j in range(1,n+1): # 1부터 입력값(N)까지의 숫자를 반복해서
    a = list(map(int, str(j))) #각 자리 수를 분리하여 리스트(a)에 넣어 준다.
    s = set() #리스트(a)에 담긴 숫자들의 공차를 넣을 집합(s) 설정
    for i in range(len(a)-1) : #리스트(a) 숫자간의 공차를 구하기 위한 반복 
        s.add(a[i] - a[i+1]) #리스트 숫자간에 공차를 집합(s)에 추가
        
    if len(s) == 1 or len(s) == 0 : # 중복이 없는 집합(s)의 개체가 1개 혹은 0개라면
        cnt += 1 #한수가 맞기때문에 +1
print(cnt) 
            
