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

    #add a node at the end of a linked list
    def append(self,data):
        element=NODE(data)
        self.last=element
        self.length +=1
        return element

    #add a node at the start of a linked list and make it head
    def prepend(self,data):
        element = NODE(data)
        element.next=self.head
        self.head=element
        self.length+=1


    #add a node after a specific node of a linked list
    #it excepts the node after which we want to add a new node and the data of the new node
    #you can pass a node object or the position of the node after which you want to add a new node
    #NOTE:: unlike list or tuple, it begains at 1
    def insertAfter(self,position: NODE|int,data,next=None):
        if self.length <1:
            return None
        #if position is an NODE object
        elif isinstance(position,NODE):
            element=NODE(data)
            element.next=position.next
            position.next=element
            self.length+=1
        #if position is an index number
        elif isinstance(position,int) and position<=self.length:
            current=self.head
            count=1
            while count!=position:
                current=current.next
                count+=1
            element=NODE(data)
            element.next=current.next
            current.next=element
            self.length+=1
        else:
            return None
        return element

    #remove first node and make the second one head
    def remfirst(self):
        self.head=self.head.next

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
            self.length-=1

    #get max element 
    def getMax(self):
        if self.length<1:
            return None
        elif self.length==1:
            return self.last
        elif self.length==2:
            return max(self.head.data, self.last.data)
        else:
            current=self.head
            currentAfter = self.head.next
            count=1
            while count<=self.length-1:
                if current.data >= currentAfter.data:
                    currentAfter = currentAfter.next
                else:
                    current =  current.next
                    currentAfter = currentAfter.next
                    print(count,' your here')
                count+=1
            return current.data



    