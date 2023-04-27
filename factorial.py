def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("enter a number"))
result=factorial(number)
for i in range(1,result+1):
    print(i,end=",")
