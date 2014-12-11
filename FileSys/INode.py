__author__ = 'adri'


class INode():

    def __init__(self, name):
        self.name = name
        self.pointer = []

    def add_pointer(self, pointer):
        self.pointer.append(pointer)