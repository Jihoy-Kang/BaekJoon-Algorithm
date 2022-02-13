#내풀이
croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

a = input()

for i in croatia :
    a = a.replace(i,'*')

print(len(a))



#모범답안
word = ["c=", "c-", "dz=", "d-","lj", "nj", "s=", "z="]

input_data = input()
count = 0

for i in word:
    input_data = input_data.replace(i, '*')

print(len(input_data))


