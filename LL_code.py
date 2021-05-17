class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode_end(self,val):
        self.nnode=Node(val)
        if self.head==None:
            self.head=self.nnode
            self.tail=self.nnode
        else:
            self.tail.next=self.nnode
            self.tail=self.tail.next
    def display(self):
        temp=self.head
        if(temp==None):
            print(" No nodes")
        else:
            while(temp):
                print(temp.val,end=" ")
                temp=temp.next
    def delete_end(self):
        temp=self.head
        if(temp==None):
            print(" No nodes")
        else:
            while(temp.next.next):
                temp=temp.next
            temp.next=None
            self.tail=temp
    def delete_front(self):
        temp=self.head
        if(temp==None):
            print(" No nodes")
        else:
            temp=temp.next
            self.head.next=None
            self.head=temp
    def addNode_beg(self,val):
        self.nnode=Node(val)
        if self.head==None:
            self.head=self.nnode
            self.tail=self.nnode
        else:
            self.nnode.next=self.head
            self.head=self.nnode
    def addNode_pos(self,pos,val):
        self.nnode=Node(val)
        
        if self.head==None:
            self.head=self.nnode
            self.tail=self.nnode
        else:
            if(pos==1):
                self.addNode_beg(val)
            else:
                temp=self.head
                i=1
                while(i<pos-1 and temp):#1<3 
                    temp=temp.next
                    i+=1
                if(temp):
                    self.nnode.next=temp.next
                    temp.next=self.nnode
                else:
                    print("Not in range")
    def deleteNode_pos(self,pos):
        temp=self.head
        if(temp==None):
            print(" No nodes")
        else:
            if(pos==1):
                self.delete_front()
            else:
                i=1
                while(i<pos-1 and temp):
                    temp=temp.next
                    i+=1
                if(temp):
                    temp.next=temp.next.next
                else:
                    print("not in range")
                
        
        
ll=LinkedList()
ll.addNode_end(100)
ll.addNode_end(200)
ll.addNode_end(300)
ll.addNode_end(400)
ll.addNode_beg(500)
ll.addNode_pos(1,700)
ll.display()
print()
ll.deleteNode_pos(10)
ll.display()


        
