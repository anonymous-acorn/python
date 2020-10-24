import random as r
print("1부터 10까지의 수")

sungjuk=[1,2,3,4,5,6,7,8,9,10]
result=0
print(sungjuk[0])
print(sungjuk[1])
print(sungjuk[2])
print(sungjuk[3])
print(sungjuk[4])
print(sungjuk[5])
print(sungjuk[6])
print(sungjuk[7])
print(sungjuk[8])
print(sungjuk[9])

print("----------")

for x in range (10):
    result=result+sungjuk[x]
print("1부터 10까지의 수의 합은",result)
print("1부터 10까지의 수의 평균은",result/10)
print("1부터 10까지의 수중 하나를 뽑을게 음..... 그래!",r.choice(sungjuk),"(으)로 뽑았어!")
