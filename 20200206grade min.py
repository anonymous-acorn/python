grade=[11,22,33,44,55,66,77,88,99]


min=grade[0]
for x in range(9):
    if min>grade[x]:
        min=grade[x]
        print(min)
print("위 수 중에 가장 작은 수는",min,"입니다.")
