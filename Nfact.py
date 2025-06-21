#without recursion
'''def Fact(n) :
    if(n==1) :
        return 1
    fact=1

    for i in range(n,0,-1):
        print(i)
        fact = fact*i

    return fact

print(Fact(4))'''


#with recurion
def fact(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n*fact(n-1)

n=4
print(fact(n));










