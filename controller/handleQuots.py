class Quote:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next quote in DLL
        self.prev = prev # reference to previous quote in DLL
        self.data = data

# Class to create a Doubly Linked List
class DoublyLinkedList:
 
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    # Adding a quote at the front of the list
    def insertQuoteAtFront(self, newData):
    
        # 1 & 2: Allocate the quote & Put in the data
        newQuote = Quote(data = newData)
    
        # 3. Make next of new quote as head and previous as NULL
        newQuote.next = self.head
        newQuote.prev = None
    
        # 4. change prev of head quote to new quote
        if self.head is not None:
            self.head.prev = newQuote
    
        # 5. move the head to point to the new quote
        self.head = newQuote

    # Given a quote as prevQuote, insert
    # a new quote after the given quote
    def insertQuoteAfterGivenQuote(self, prevQuote, newData):
    
        # 1. check if the given prevQuote is NULL
        if prevQuote is None:
            print("This quote doesn't exist in DLL")
            return

        #2. allocate quote  & 3. put in the data
        newQuote = Quote(data = newData)

        # 4. Make next of new quote as next of prevQuote
        newQuote.next = prevQuote.next

        # 5. Make the next of prevQuote as newQuote
        prevQuote.next = newQuote

        # 6. Make prevQuote as previous of newQuote
        newQuote.prev = prevQuote

        # 7. Change previous of newQuote's next quote */
        if newQuote.next is not None:
            newQuote.next.prev = newQuote

    # Add a quote at the end of the DLL
    def insertQuoteAtEnd(self, newData):
    
        # 1. allocate quote 2. put in the data
        newQuote = Quote(data = newData)
        last = self.head

        # 3. This new quote is going to be the
        # last quote, so make next of it as NULL
        newQuote.next = None

        # 4. If the Linked List is empty, then
        #  make the new quote as head
        if self.head is None:
            newQuote.prev = None
            self.head = newQuote
            return

        # 5. Else traverse till the last quote
        while (last.next is not None):
            last = last.next

        # 6. Change the next of last quote
        last.next = newQuote
        # 7. Make last quote as previous of new quote */
        newQuote.prev = last

    # This function prints contents of linked list
    # starting from the given node
    def printList(self, node):
 
        print("\nTraversal in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node.next
 
        print("\nTraversal in reverse direction")
        while last:
            print(" {}".format(last.data))
            last = last.prev
 
# Driver program to test above functions
 
 
# Start with empty list
llist = DoublyLinkedList()
 
# Insert 6. So the list becomes 6->None
llist.insertQuoteAtEnd({"type": "TSE"})
 
# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.insertQuoteAtFront({"type": "SBIJ"})
 
# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.insertQuoteAtFront({"type": "CHIX"})
 
# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.insertQuoteAtFront({"type": "TSE"})
 
# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.insertQuoteAfterGivenQuote(llist.head.next, {"type": "SBIJ"})
 
print ("Created DLL is: ")
llist.printList(llist.head)