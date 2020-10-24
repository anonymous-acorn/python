def sum_01(a):
    s=0
    for x in range(1,a+1):
        s=s+x
    return s

print("1부터 10까지의 수를 모두 더한값:",sum_01(10))
print("1부터 100까지의 수를 모두 더한 값:",sum_01(100))
