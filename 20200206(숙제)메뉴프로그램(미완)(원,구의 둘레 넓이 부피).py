while True:
    print("=============================\n");
    print("==   1. 원의 둘레 구하기   ==\n");
    print("==   2. 원의 넓이 구하기   ==\n");
    print("==   3. 구의 부피 구하기   ==\n");
    print("==   4. 그만두기           ==\n");
    print("=============================\n");

    s=int(input("1,2,3,4중 선택하세요:"))


    if s==4:
       print("쳇 아 더러워~!")
       break

    if s==1 or s==2 or s==3 or s==4 or s==5:
        loop=int(input("원의 반지름은 몇?:")) 
        number=int(input(":"))

    if s==1:
        print("원의 둘레를 출력하는중.")
        for x in range(1,loop+1):
            print("출력한 값은",x,"입니다.")

    elif s==2:
        print("원의 넓이를 출력하는 중.")
        for x in range(1,loop+1):
            if x%2==0:
                print("출력한 값은",x,"입니다.")

    elif s==3:
        print("홀수값을 출력하는중.")
        for x in range(1,loop+1):
            if x%2==1:
                print("출력한 값은",x,"홀수입니다.")

    

    else:
         print("제대로 말해 어쨌든 간다 아디우스~!")
         break
        
           


