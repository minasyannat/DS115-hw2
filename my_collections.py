from abc import ABC, abstractmethod


class Collection(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def empty(self) -> None:
        pass

    @abstractmethod
    def size(self) -> int:
        pass
# add_first(e: object)
# remove_first()-> bool
# add_last(e: object) -> None
# remove_last()-> bool
# first()-> object
# last() -> object
# replace(e: object, r: object)-> bool # replaces the first
# # occurrence of e in List with r and returns true
# add_at(e: object, index: int) -> bool
# get_at(index: int) -> object
# remove_at(index: int) -> object


class List(Collection):
    @abstractmethod
    def add_first(self, e: object):
        pass

    @abstractmethod
    def remove_first(self) -> bool:
        pass

    @abstractmethod
    def add_last(self, e: object) -> None:
        pass

    @abstractmethod
    def remove_last(self) -> bool:
        pass

    @abstractmethod
    def first(self) -> object:
        pass

    @abstractmethod
    def last(self) -> object:
        pass

    @abstractmethod
    def replace(self, e: object, r: object) -> bool:
        pass

    @abstractmethod
    def add_at(self, e: object, index: int) -> bool:
        pass

    @abstractmethod
    def get_at(self, index: int) -> object:
        pass

    @abstractmethod
    def remove_at(self, index: int) -> object:
        pass

# Stack(Collection):
# push(e: object) -> None
# pop() -> object
# top() -> object

class Stack(Collection):

    @abstractmethod
    def push(self, e: object) -> None:
        pass

    @abstractmethod
    def pop(self) -> object:
        pass

    @abstractmethod
    def top(self) -> object:
        pass


class LinkedList(List):

    class _Node:

        def __init__(self, value: object, ref = None):
            self.data = value
            self.next = ref

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def empty(self) -> None:
        self.__first = self.__last = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def add_first(self, e: object) -> None:
        if self.__size == 0:
            new_node = self._Node(e)
            self.__first = self.__last = new_node
        else:
            new_node = self._Node(e, self.__first)
            self.__first = new_node
        self.__size += 1

    def remove_first(self) -> bool:
        if self.__size == 0:
            raise Exception("Empty list")
        elif self.__size == 1:
            self.__first = self.__last = None
            self.__size = 0
        else:
            self.__first = self.__first.next
            self.__size -= 1

    def add_last(self, e: object) -> None:
        if self.__size == 0:
            new_node = self._Node(e)
            self.__first = self.__last = new_node
        else:
            new_node = self._Node(e)
            self.__last.next = new_node
        self.__size += 1

    def remove_last(self) -> bool:
        if self.__size == 0:
            raise Exception("Empty list")
        elif self.__size == 1:
            self.__first = self.__last = None
            self.__size = 0
        else:
            self.__last = None
            self.__size -= 1

    def first(self) -> object:
        return self.__first.data

    def last(self) -> object:
        return self.__last.data

    def replace(self, e: object, r: object) -> bool:
        if self.__size == 0:
            raise Exception("Empty list")
        tmp = self.__first
        while tmp:
            if tmp.data == e:
                tmp.data = r
                break
            tmp = tmp.next

    def add_at(self, e: object, index: int) -> bool:
        if self.__size == 0:
            raise Exception("Empty list")
        if index == 0:
            return self.add_first(e)
        else:
            tmp = self.__first
            prev = None
            while tmp and index > 0:
                tmp, prev = tmp.next, tmp
                index -= 1
            new_node = self._Node(e, tmp)
            prev.next = new_node

    def get_at(self, index: int) -> object:
        if self.__size == 0:
            raise Exception("Empty list")
        if index == 0:
            return self.first()
        else:
            tmp = self.__first
            while tmp and index > 0:
                tmp = tmp.next
                index -= 1
            return tmp.data

    def remove_at(self, index: int) -> object:
        if self.__size == 0:
            raise Exception("Empty list")
        if index == 0:
            return self.remove_first()
        else:
            tmp = self.__first
            prev = None
            while tmp and index > 0:
                tmp, prev = tmp.next, tmp
                index -= 1
            prev.next = tmp.next


class DoubleLinkedList(List):

    class _Node:

        def __init__(self, value: object, ref = None, prev = None):
            self.data = value
            self.next = ref
            self.prev = prev

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def empty(self) -> None:
        self.__first = self.__last = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def add_first(self, e: object):
        if self.__size == 0:
            new_node = self._Node(e)
            self.__first = self.__last = new_node
        else:
            new_node = self._Node(e, self.__first)
            self.__first = new_node
        self.__size += 1

    def remove_first(self) -> bool:
        if self.__size == 0:
            raise Exception("Empty list")
        elif self.__size == 1:
            self.__first = self.__last = None
            self.__size = 0
        else:
            self.__first = self.__first.next
            self.__size -= 1
            return True

    def add_last(self, e: object) -> None:
        if self.__size == 0:
            new_node = self._Node(e)
            self.__first = self.__last = new_node
        else:
            self.__last.next = self._Node(e)
        self.__size += 1

    def remove_last(self) -> bool:
        if self.__size == 0:
            raise Exception("Empty list")
        elif self.__size == 1:
            self.__first = self.__last = None
            self.__size = 0
        else:
            self.__last.prev.next = None
            self.__size -= 1
            return True

    def first(self) -> object:
        return self.__firt.data

    def last(self) -> object:
        return self.__last.data

    @abstractmethod
    def replace(self, e: object, r: object) -> bool:
        pass

    @abstractmethod
    def add_at(self, e: object, index: int) -> bool:
        pass

    @abstractmethod
    def get_at(self, index: int) -> object:
        pass

    @abstractmethod
    def remove_at(self, index: int) -> object:
        pass








