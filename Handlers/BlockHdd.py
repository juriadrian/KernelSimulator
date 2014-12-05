__author__ = 'adri'


class BlockHdd:

    def __init__(self, program_name, block_size=10):
        self.program_name = program_name
        self.instructions = []
        self.block_size = block_size

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def check_size(self):
        while self.instructions.__len__() <= self.block_size:
            self.instructions.append(None)