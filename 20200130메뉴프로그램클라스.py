while True:
    print("======================")
    print("== 1번 정수 출력하기== ")
    print("== 2번 짝수 출력하기== ")
    print("== 3번 홀수 출력하기== ")
    print("== 4번 배수 출력하기== ")
    print("== 5번 약수 출력하기== ")
    print("===== 6번 그만하기=====")
    print("======================")

    s=int(input("메뉴를 선택하세요:"))


    if s==6:
       print("Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye Bye.")
       break

    if s==1 or s==2 or s==3 or s==4 or s==5:
        loop=int(input("반복할 값은?:")) 
        number=int(input("숫자 값은?:"))

    if s==1:
        print("정수값을 출력하는중.")
        for x in range(1,loop+1):
            print("출력한 값은",x,"입니다.")

    elif s==2:
        print("짝수값을 출력하는중.")
        for x in range(1,loop+1):
            if x%2==0:
                print("출력한 값은",x,"짝수입니다.")

    elif s==3:
        print("홀수값을 출력하는중.")
        for x in range(1,loop+1):
            if x%2==1:
                print("출력한 값은",x,"홀수입니다.")

    elif s==4:
        print("배수값을 출력하는중.")
        for x in range(1,loop+1):
            if x%number==0:
                print(number,"의 배수값은",x,"입니다.")

    elif s==5:
        print("약수값을 출력하는중.")
        for x in range(1,number+1):
            if number%x==0:
                print(number,"의 약수값은",x,"입니다.")

    else:
        print("못알아 듣겠어. Bye Bye.")
        break
        
           


