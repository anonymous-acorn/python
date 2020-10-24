n=int(input("약수를 구하고 싶은 수를 입력하세요.(1000000000000이상의 수를 입력하면 계산하는데 시간이 많이 걸립니다.)"))
count=0
total=0
for x in range(1,n+1):
    if n%x==0:
        print(x,"는",n,"의 약수입니다.")
        total=total+x
        count=count+1
print("약수 값의 총 합은 ",total,"입니다.")
print("약수의 총 개수는",count,"입니다.")      
