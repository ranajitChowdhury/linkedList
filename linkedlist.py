#this page holds all the nesesory tools to work with linked list

#NODE class
#it is like an element of a list
class NODE:
    def __init__(self,data):
        self.data=data #data of the node
        #self.pre=previous #previous node of the node
        self.next=None #next node of the node

#Linked list class 
class linkedList:
    def __init__(self):
        self.head=None #head of a linked List
        self.last=None #last node of a linked list
        self.length=0 #length of a linked list

    #append a node in a linked list 
    def append(self,data):
        element=NODE(data)
        self.last=element
        self.length +=1
        return element

    #delete last node of a linked list
    def pop(self):
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.legth=0
        else:
            current=self.head
            while current.next!=self.last:
                current =  current.next 
            current.next=None
            self.last=current

