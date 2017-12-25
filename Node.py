from CustomDataStructures import Element
from typing import TypeVar

T = TypeVar('T')


class Node(Element[T]):

    def __init__(self, data: T):
        super().__init__(data)
        self.next = None
        self.prev = None

    def setPrev(self, node: Element) -> bool:
        self.prev = node
        return True

    def setNext(self, node: Element) -> bool:
        self.next = node
        return True

    def getPrev(self) -> Element:
        return self.prev

    def getNext(self) -> Element:
        return self.next

