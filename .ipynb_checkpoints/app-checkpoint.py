#import linkedList
from linkedlist import linkedList

#
ll=linkedList()
node1=ll.append(100)
ll.head=node1
node2=ll.append(200)
node1.next=node2
node3=ll.append(300)
node2.next=node3
node4=ll.append(400)
node3.next=node4
node5=ll.append(500)
node4.next=node5

node6=ll.insertAfter(3,6661)
node7=ll.insertAfter(node1,101)
#ll.pop()
#ll.prepend(200)
#ll.remfirst()
print(ll.getMax())
# print(ll.head.next.data)
# print(ll.head.next.next.data)
# print(ll.head.next.next.next.data)
# print(ll.head.next.next.next.next.data)
# print(ll.head.next.next.next.next.next.data)
# print(ll.head.next.next.next.next.next.next.data)