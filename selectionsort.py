list1=[56,0,2,2,6,0]
print(list1)
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_ind=list1.index(min_val,i)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]
print(list1)
