list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
count=0
sum1=0
sum2=0
prd=1
sum1=sum(list1)
sum2=sum(list2)
if (sum1==sum2):
    print(1)
else:
    for i in len(list1):
        k=list1[i]
        list[i]=list[2]
        list[2]=k
        sum1=sum(list1)
        sum2=sum(list2)
        if (sum1==sum2):
            count+=1
            prd=list1[i]*list2[i]
