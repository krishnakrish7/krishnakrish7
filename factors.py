def factors(n):
    for i in range(2,int(n**0.5)):
        if(n%i==0):
            print(i,end=" ")
            if(n//i!=i):
                print(n//i,end=" ")
n=int(input())
factors(n)
print(list(factors[n]))

