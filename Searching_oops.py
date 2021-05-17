class Search:
    def __init__(self,data,key):
        self.data=data
        self.key=key
    def linearsearch(self):
        for i in range(len(self.data)):
            if(self.key==self.data[i]):
                print("Element Found")
                break
        else:
            print("Element is not Found")
    def binarysearch(self):
        l=0
        h=len(self.data)-1
        ic=0
        while(l<=h):
            ic+=1
            m=(l+h)//2
            if(self.data[m]==self.key):
                print("Element is Found")
                break
            elif(self.data[m]<self.key):
                l=m+1
            else:
                h=m-1
        else:
            print("Element Not found")
        print(ic)
                
obj=Search([1,2,3,4,5,6,7,8,9],9)
obj.binarysearch()








"""
ds:
binary search
selection sort
insertion sort
bubble sort
hashing
stack
queue
linkedlist

1 2 3 4 5 6 7 8 9 
"""
