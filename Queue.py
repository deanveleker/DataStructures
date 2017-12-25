from typing import TypeVar, Generic

from CustomDataStructures import Stack

T = TypeVar('T')


class Queue(Generic[T]):

    def __init__(self):
        self.inputStack = Stack()
        self.outputStack = Stack()

    def enqueue(self, item: T):
        self.inputStack.push(item)

    def dequeue(self):

        if self.outputStack.size > 0:
            return self.outputStack.pop()

        while self.inputStack.size > 0:
            self.outputStack.push( self.inputStack.pop() )

        return self.outputStack.pop()
