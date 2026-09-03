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
    def __itit__(self):
        self.head=None #head of a linked List
        self.last=None #last node of a linked list
        self.length=0 #length of a linked list

    #append a node in a linked list 
    def append(self,data):
        element=NODE(data)
        self.last=element
        self.length +=1


