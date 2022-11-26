# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # add nodes

    def put(self, val):
        if self.head == None:
            self.head = Node(val)
            return self
        curr = self.head
        while curr.next != None: # iterate through list until next equals None.
            curr = curr.next
        curr.next = Node(val) # if next equals None, make next equal to Node value.
        return self

    # delete duplicate method

    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    # display list

    def display_values(self):
        if self.head == None: # check if head is empty
            print("This list is empty")
        else:
            curr = self.head
            while curr != None:
                print(curr.val)
                curr = curr.next
        return self

# examples

x = LinkedList()
x.head = Node(1)

# add nodes with duplicates 3's.
x.put(2).put(3).put(3).put(4)

# delete duplicates with head as argument and display list.
x.deleteDuplicates(x.head)
x.display_values()