#가장많이 사용한 알파벳이 두개이상이면 ?출력
#대소문자 구분없음
#대문자 출력

s = list(map(str, input()))
new = []
cnt = []

for i in s :
    new.append(i.upper())

for i in new :    
    cnt.append(new.count(i))

print(new)
print(cnt)
