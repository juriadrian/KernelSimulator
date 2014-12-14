__author__ = 'adri'


class File():

    def __init__(self, file_name, inode):
        self.name = file_name
        self.inode = inode


class INode():

    def __init__(self, name):
        self.name = name
        self.pointer = []

    def add_pointer(self, pointer):
        self.pointer.append(pointer)


class Data():

    def __init__(self, program_name, size):
        self.program_name = program_name
        self.actual_key = None
        self.blocks = {} #Dictionary where the key is the sector in the hard disk and the value is in which block is allocated the instruction
        self.size = size

    def save_data(self, key, value):
        if key != self.actual_key:
            self.blocks[key] = []
            self.actual_key = key
        self.blocks[key].append(value)

