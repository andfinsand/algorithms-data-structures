# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # add values

    def put(self, val):
        if self.head == None:
            self.head = Node(val)
            return self
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(val)
        return self

    # merge two lists

    def mergeTwoLists(self, list1, list2):
        dummy = curr = Node(0)
        head1 = list1.head
        head2 = list2.head

        while list1 and list2:
            if head1.val < head2.val:
                curr.next = head1
                list1 = head1.next
            else:
                curr.next = head2
                list2 = head2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next

    # print values

    def display_values(self):
        if self.head == None:
            return "List is empty."
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        return self

# examples

# initialize list1
list1 = LinkedList()
list1.head = Node(1)
list1.put(2)
list1.put(4)
print("List 1:" )
list1.display_values()

print("")

# initialize list2
list2 = LinkedList()
list2.head = Node(1)
list2.put(3)
list2.put(4)
print("List 2:" )
list2.display_values()

print("")

# merge sorted lists
list3 = LinkedList()
list3.head = Node(0)
list3.mergeTwoLists(list1, list2)
print("Merged lists:" )
list3.display_values()