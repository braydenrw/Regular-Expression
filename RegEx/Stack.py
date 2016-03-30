__author__ = 'braydenrw'


class Stack:
    def __init__(self):
        self.__storage = []

    def __len__(self):
        return self.__storage.__len__()

    def push(self, obj):
        self.__storage.append(obj)

    def pop(self):
        return self.__storage.pop()
