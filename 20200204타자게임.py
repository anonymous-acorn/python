import random as r
import time as t

Q=["apple","pineapple","banana","석류","파인애플","사과","바나나","용과","mango","코코넛"]
n=1
print("[타자게임]준비되면 Enter 키를 누르세요!")
input()
start=t.time()

s=r.choice(Q)
while n<=5:
    print("문제",n)
    print(s)
    x=input()
    if s==x:
        print("통과")
        n=n+1
        s=r.choice(Q)
    else:
        print("틀렸습니다.")
end=t.time()
et=end-start
et2=format(et,"2f")
print("타자시간:",et2,"초")
