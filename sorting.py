class Sorting:
    def __init__(self,data):
        self.data=data
    def selection_sort(self):
        pas=0
        for i in range(len(self.data)-1,-1,-1):
            pas+=1
            me=i
            for j in range(i-1,-1,-1):
                if(self.data[me]<self.data[j]):
                    me=j
            temp=self.data[me]
            self.data[me]=self.data[i]
            self.data[i]=temp
            print(pas,"-->",self.data)
        #print(self.data)


    
data=[11,7,12,14,19,1,6,18,8,16]
obj=Sorting(data)
obj.selection_sort()








"""
11 7 12 14 19 1 6 18 8 16


pass1:11 7 12 14 16 1 6 18 8 19

pass2:11 7 12 14 16 1 6 8 18 19

pass3:11 7 12 14 8 1 6 16 18 19

pass4:11 7 12 6 8 1 14 16 18 19

pass5:11 7 1 6 8 12 14 16 18 19

pass6:8 7 1 6 11 12 14 16 18 19

pass7:6 7 1 8 11 12 14 16 18 19

pass8:6 1 7 8 11 12 14 16 18 19

pass9:1 6 7 8 11 12 14 16 18 19

"""
