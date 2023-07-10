def fact(num):
    if num==0:
        print('Factorial of zero can not find')
    elif num == 1:
        return 1
    else:
        return num*fact(num-1)

factorial = fact(4)
print("Factorial of num is : ",factorial)