while True:

    print("***********************WELCOME TO CALCI**************************")
    print("Please Enter 2 numbers")

    num1 = input("Enter 1st number \n");
    if num1.lower()=="exit":
        break
    num1 = float(num1);
    num2 = input("Enter 2nd number \n");
    num2 = float(num2);
    operator = input("enter the operator -> +,-,*,/");

    if operator=="+":
        print("Result = ",num1+num2);
    elif operator=="-":
        print("Result = ",num1-num2);
    elif operator=="*":
        print("Result = ",num1*num2);
    elif operator=="/":
        print("Result = ",num1/num2);
    else:
        print("Invalid Operator");
