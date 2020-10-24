day=int(input("날짜를 입력하세요."))

car=[0,0,0,0,0]

car[0]=int(input("첫 번째 차량의 끝자리 번호"))
car[1]=int(input("두 번째 차량의 끝자리 번호"))
car[2]=int(input("세 번째 차량의 끝자리 번호"))
car[3]=int(input("네 번째 차량의 끝자리 번호"))
car[4]=int(input("다섯 번째 차량의 끝자리 번호"))

count=0

for x in range(5):
    if day==car[x]:
        count=count+1
print("위반한 차량은 ",count,"대 입니다.")
