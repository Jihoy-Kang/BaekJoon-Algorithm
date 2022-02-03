#내 풀이
s = list(map(str, input()))
new = []
cnt = []
max_num = 0
max_chr = set()

for i in s :
    new.append(i.upper())

for i in new :
    if max_num < new.count(i) :
        max_num = new.count(i)
        max_chr = set(i)
        print(max_chr)
    elif max_num == new.count(i) :
        max_num = new.count(i)
        max_chr.add(i)
        print(max_chr)
    else :
        continue

if len(max_chr) >= 2 :
    print('?')
else :
    print(max_chr)

#모범답안
word = input().upper()
word_list = list(set(word))
cnt = []

for i in word_list :
    cnt.append(word.count(i))

if cnt.count(max(cnt)) >= 2 :
    print('?')
else :
    print(word_list[cnt.index(max(cnt))])




