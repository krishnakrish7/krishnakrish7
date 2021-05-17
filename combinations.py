array=[1.9,8,5,6,27]
a=25
for i in range(len(array)):
    for j in range(i+1,len(array)):
        for k in range(j+1,len(array)):
            print(array[i],array[j],array[k])
