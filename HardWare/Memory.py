__author__ = 'Pato'


class Memory:

    def __init__(self):
        self.cells = []
        self.size_of_memory = 500
        self.next_cell = 0

    def read(self):
        pass

    def get_instruction_of_cell(self, index):
        return self.cells.__getitem__(index)

    def change_instruction_cell(self, from_index, to_index):
        self.cells[to_index] = self.cells[from_index]
        self.cells[from_index] = None
