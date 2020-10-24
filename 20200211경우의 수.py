import random as r

total=int(input("반복 횟수 입력"))
e=0

for x in range(total):
    if r.randint(1,6)==4:
        e=e+1

print(e/total)
