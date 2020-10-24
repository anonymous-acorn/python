day=int(input("날짜를 입력하세요."))

car=[0,0,0,0,0]

car[0]=int(input("첫 째 차의 끝자리 번호"))
car[1]=int(input("둘 째 차의 끝자리 번호"))
car[2]=int(input("셋 째 차의 끝자리 번호"))
car[3]=int(input("넷 째 차의 끝자리 번호"))
car[4]=int(input("다섯 째 차의 끝자리 번호"))

number=0

for x in range(5):
    if day==car[x]:
        number=number
print("위반한 차량은 ",number,"대.")
