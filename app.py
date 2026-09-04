#import linkedList
from linkedlist import linkedList

#
ll=linkedList()
node1 = ll.append(3)
ll.head = node1
node2 = ll.append(3)
node1.next = node2
node3 = ll.append(4)
node2.next = node3
node4 = ll.append(5)
node3.next = node4
node5 = ll.append(5)
node4.next = node5
node6 = ll.append(6)
node5.next = node6
node7 = ll.append(6)
node6.next = node7
node8 = ll.append(6)
node7.next = node8
node9 = ll.append(6)
node8.next = node9
node10 = ll.append(6)
node9.next = node10
node11 = ll.append(6)
node10.next = node11
node12 = ll.append(6)
node11.next = node12
node13 = ll.append(10)
node12.next = node13
node14 = ll.append(11)
node13.next = node14
node15 = ll.append(11)
node14.next = node15
ll.read()
ll.remduplicates()
ll.read()