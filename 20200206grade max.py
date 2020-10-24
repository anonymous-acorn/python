grade=[11,22,33,44,55,66,77,88,99]


max=grade[0]
for x in range(9):
    if max<grade[x]:
        max=grade[x]
        print(max)
print("위 수 중에 가장 큰 수는",max,"입니다.")
