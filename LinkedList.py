from typing import TypeVar, Generic

from CustomDataStructures import Node

T = TypeVar('T')


class LinkedList(Generic[T]):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        cur = self.head
        while (cur != None):
            yield cur.getData()
            cur = cur.getNext()

    def add(self, ele: T) -> bool:
        # Appends the specified element to the end of this list.
        node = Node(ele)
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            node.setPrev(self.tail)
            self.tail.setNext(node)
            self.tail = node
        self.size += 1
        return True

    def addAtIdx(self, idx: int, ele: T):
        # Inserts the specified element at the specified position in this list.

        node = Node(ele)
        if idx == 0:
            # the element to be inserted will be the new head
            node.setNext(self.head)
            if self.head != None:
                self.head.setPrev(node)
            self.head = node
        elif idx == self.size:
            # the index happens to be immediately after the tail (and will become the new tail)
            node.setPrev(self.tail)
            self.tail.setNext(node)
            self.tail = node
        elif idx > 0 and idx <= self.size:
            # trying to add to a negative index or further than the allowable bounds
            cur = self.head
            for i in range(0, idx):
                cur = cur.getNext()

            prev = cur.getPrev()
            next = cur.getNext()

            prev.setNext(cur)
            node.setPrev(prev)
            node.setNext(next)
            next.setPrev(cur)

        self.size += 1

    def addFirst(self, ele: T):
        # Inserts the specified element at the beginning of this list.
        node = Node(ele)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.setNext(self.head)
            self.head.setPrev(node)
            self.head = node
        self.size += 1

    def addLast(self, ele: T):
        # Appends the specified element to the end of this list.
        node = Node(ele)
        if self.tail == None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.setNext(node)
            node.setPrev(self.tail)
            self.tail = node
            self.size += 1

    def clear(self):
        # Removes all of the elements from this list.
        self.head = None
        self.tail = None
        self.size = 0

    def contains(self, ele: T) -> bool:
        # Returns true if this list contains the specified element.
        cur = self.head
        while (cur != None):
            if cur.getData() == ele:
                return True
            cur = cur.getNext()
        return False

    def element(self) -> T:
        # Retrieves, but does not remove, the head (first element) of this list.
        return self.head.getData()

    def get(self, index: int) -> T:
        # Returns the element at the specified position in this list.
        cur = self.head
        idx = 0
        while (idx < index):
            cur = cur.getNext()
            idx += 1
        return cur.getData()

    def getFirst(self) -> T:
        # Returns the first element in this list.
        if self.head != None:
            return self.head.getData()

    def getLast(self) -> T:
        # Returns the last element in this list.
        if self.tail != None:
            return self.tail.getData()

    def indexOf(self, obj: object) -> int:
        # Returns the index of the first occurrence of the specified element in this list, or -1 if this list does not contain the element.
        cur = self.head
        idx = 0
        while (cur != None):
            if cur.getData() == obj:
                return idx
            cur = cur.getNext()
            idx += 1
        return -1

    def lastIndexOf(self, obj: object) -> int:
        # Returns the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element.
        cur = self.head
        idx = 0
        lastIdx = -1
        while (cur != None):
            if cur.getData() == obj:
                lastIdx = idx
            cur = cur.getNext()
            idx += 1
        return lastIdx

    def listIterator(self, index: int):
        # Returns a list-iterator of the elements in this list (in proper sequence), starting at the specified position in the list.
        cur = self.get(index)
        while (cur != None):
            yield cur.getData()
            cur = cur.getNext()

    def peek(self) -> T:
        # Retrieves, but does not remove, the head (first element) of this list.
        return self.head.getData()

    def peekFirst(self) -> T:
        # Retrieves, but does not remove, the first element of this list, or returns null if this list is empty.
        return self.head.getData()

    def peekLast(self) -> T:
        # Retrieves, but does not remove, the last element of this list, or returns null if this list is empty.
        return self.tail.getData()

    def poll(self) -> T:
        # Retrieves and removes the head (first element) of this list.
        head = self.head
        if head == None:
            return T(None)
        if head.getNext() == None:
            self.head = None
            self.tail = None
        else:
            head.getNext().setPrev(None)
            self.head = head.getNext()
        self.size -= 1
        return head.getData()

    def pollFirst(self) -> T:
        # Retrieves and removes the first element of this list, or returns null if this list is empty.
        return self.poll()

    def pollLast(self) -> T:
        # Retrieves and removes the last element of this list, or returns null if this list is empty.
        tail = self.tail
        newTail = self.tail.getPrev()
        if newTail == None:
            self.head = None
            self.tail = None
        else:
            newTail.setNext(None)
            self.tail = newTail
        self.size -= 1
        return tail.getData()

    def pop(self) -> T:
        # Pops an element from the stack represented by this list.
        return self.removeLast()

    def push(self, ele: T):
        # Pushes an element onto the stack represented by this list.
        self.addLast(ele)

    def remove(self) -> T:
        # Retrieves and removes the head (first element) of this list.
        if self.size > 0:
            head = self.head
            nodeAfter = head.getNext()
            if nodeAfter != None:
                nodeAfter.setPrev(None)
            self.head = nodeAfter
            self.size -= 1
            return head.getData()

    def removeAtIdx(self, idx: int) -> T:
        # Removes the element at the specified position in this list.
        cur = self.head
        prev = None
        i = 0
        while (cur != None):

            if i == idx:
                next = cur.getNext()
                if self.head == cur:
                    next.setPrev(prev)
                    self.head = next
                elif self.tail == cur:
                    prev.setNext(next)
                    self.tail = prev
                else:
                    prev.setNext(next)
                    next.setPrev(prev)
                self.size -= 1
                return cur.getData()

            prev = cur
            cur = cur.getNext()
            i += 1

    def removeObj(self, obj: object) -> bool:
        # Removes the first occurrence of the specified element from this list, if it is present.
        cur = self.head
        prev = None
        while (cur != None):
            next = cur.getNext()
            if cur.getData() == obj:
                if cur == self.head:
                    next.setPrev(None)
                    self.head = next
                elif cur == self.tail:
                    self.tail = prev
                    prev.setNext(None)
                else:
                    prev.setNext(next)
                    next.setPrev(prev)
                self.size -= 1
                return True
            prev = cur
            cur = next
        return False

    def removeFirst(self) -> T:
        # Removes and returns the first element from this list.
        if self.size > 0:
            head = self.head
            nodeAfter = head.getNext()
            if nodeAfter != None:
                nodeAfter.setPrev(None)
            self.head = nodeAfter
            self.size -= 1
            return head.getData()

    def removeFirstOccurence(self, ele: T) -> bool:
        # Removes the first occurrence of the specified element in this list (when traversing the list from head to tail).
        cur = self.head
        prev = None
        while (cur != None):
            next = cur.getNext()
            if cur.getData() == ele:
                if cur == self.head:
                    next.setPrev(None)
                    self.head = next
                elif cur == self.tail:
                    self.tail = prev
                    prev.setNext(None)
                else:
                    prev.setNext(next)
                    next.setPrev(prev)
                self.size -= 1
                return True
            prev = cur
            cur = next
        return False

    def removeLast(self) -> T:
        # Removes and returns the last element from this list.
        if self.size > 0:
            tail = self.tail
            nodeBefore = tail.getPrev()
            if nodeBefore != None:
                nodeBefore.setNext(None)
            self.tail = nodeBefore
            self.size -= 1
            return tail.getData()

    def removeLastOccurence(self, obj: object) -> bool:
        # Removes the last occurrence of the specified element in this list (when traversing the list from head to tail).
        lastIdx = self.lastIndexOf(obj)
        if lastIdx == -1:
            return False
        self.removeAtIdx(lastIdx)
        self.size -= 1
        return True

    def size(self) -> int:
        # Returns the number of elements in this list.
        return self.size

    def toArray(self) -> list():
        # Returns an array containing all of the elements in this list in proper sequence (from first to last element).
        arr = list()
        curNode = self.head
        while (curNode != None):
            arr.append(curNode.getData())
            curNode = curNode.getNext()
        return arr

    def toArrayInList(self, arr: list) -> list():
        # Returns an array containing all of the elements in this list in proper sequence (from first to last element);
        # the runtime type of the returned array is that of the specified array.
        listAsArr = self.toArray()
        newArr = list[T]()
        for ele in arr:
            if listAsArr.contains(ele):
                newArr.append(ele)
        return newArr

