__author__ = 'Pato'


class Program:

    def __init__(self, a_name):
        self.instructions = []
        self.program_name = a_name
        self.program_size = 0
        self.instructions.append('EOF')

    def run(self):
        for i in self.instructions:
            i.execute()

    def get_instructions(self):
        return self.instructions

    def add_instruction(self, instruction):
        self.instructions.insert(self.program_size, instruction)
        self.program_size += 1

    def get_program_size(self):
        return self.program_size

    def get_program_name(self):
        return self.program_name

