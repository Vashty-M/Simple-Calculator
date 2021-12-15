#Enter numbers and operator

a=float(input("Enter number:"))
operator=input("Enter operator:")
b=float(input("Enter number:"))

Add=a+b
Minus=a-b
multiply=a*b
Division=a/b

if operator=='+':
    print("The answer is", Add)

if operator=='-':
    print("The answer is", Minus)




elif  operator=='*':
    print("The answer is", multiply)


elif  operator=='/':
    print("The answer is", Division)

else:
    print("invalid operator")
