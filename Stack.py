from typing import TypeVar, Generic

from CustomDataStructures import LinkedList

T = TypeVar('T')


class Stack(LinkedList[T]):

    def __init__(self):
        super().__init__()

    def push(self, item: T):
        super().push(item)

    def pop(self) -> T:
        return super().pop()
