__author__ = 'adri'


class MemoryBlock:

    def __init__(self, init, end, id):
        self.init = init
        self.end = end
        self.id = id

    def change_init(self, index):
        self.init = index

    def change_end(self, index):
        self.end = index

    def get_size(self):
        return (self.end - self.init) + 1