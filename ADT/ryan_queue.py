class Queue():
    def __init__(self):
        self.__contents = list()

    def enqueue(self, item):
        self.__contents.append(item)

    def dequeue(self):
        return self.__contents.pop(0)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.__contents[len(self.__contents)]

    def size(self):
        return len(self.__contents)

    def clear(self):
        self.__contents = list()

    def __str__(self):
        return str(self.__contents)