cash = eval(input("Enter your cash: "))
if cash<0:
    print("wrong input")
else:
    if cash>500:
        x = cash+1000
        print(x)
    else:
        print("cash is less than 500")
