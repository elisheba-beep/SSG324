class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
        
    #insert at the end - push
    def insert_at_end(self, data):
        #create a new node with the value
        newNode = Node(data)
        #check if the linked list is empty
        if self.head is None:
            #set the new node to the head and tail of the linked list
            self.head = newNode
            self.tail = newNode
        else:
            #set the next of the tail to the new node and change the tail to the new node
            self.tail.next = newNode
            self.tail = newNode
        #add one to the length
        self.length+=1
        return self
    
    #remove at the end - pop
    def remove_at_end(self):
        #check if the list is empty
        if self.head is None:
            print("Linked list is empty")
            return
        #store the head in two variables:temp and pre
        temp = self.head
        pre = self.head
        
        #checking the next value of temp
        while temp.next:
            #set pre to temp
            pre = temp
            #set temp to the next node
            temp = temp.next
        #the tail becomes the pre(since we're removing the next one)
        self.tail = pre
        self.tail.next = None
        self.length-=1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return self
    


myList = LinkedList(7)
myList.insert_at_end(11)
myList.insert_at_end(18)
print(myList.head.next.next.data)
myList.remove_at_end()
value = myList.head
while value:
    print (value.data)
    value = value.next

    
        