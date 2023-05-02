class Node:
    def __init__(sheba, data=None, next=None):
        sheba.data = data
        sheba.next = next
        
class LinkedList:
    def __init__(sheba, value):
        newNode = Node(value)
        sheba.head = newNode
        sheba.tail = newNode
        sheba.length = 1
        
    def printList(sheba):
        node = sheba.head
        liststr = ''
        while node:
            if node.next is None:
                liststr += str(node.data)
                break
            else:
                liststr+= str(node.data) + '-->'
                node = node.next
        print(liststr)
    
    
    
newList = LinkedList(7)
newList.printList()
    