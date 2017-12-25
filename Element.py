from typing import TypeVar, Generic

T = TypeVar('T')


class Element(Generic[T]):

    def __init__(self, data: T):
        self.data = data

    def __eq__(self, other) -> bool:
        if other == None:
            return False
        return self.data == other.data

    def getData(self) -> T:
        return self.data

    def setData(self, data: T):
        self.data = data
