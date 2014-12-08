from FileSys.Data import Data
from FileSys.Folder import Folder
from Handlers.BlockHdd import BlockHdd

__author__ = 'Pato'


class HardDisk:

    def __init__(self, root):
        self.sectors = {}
        self.blocks = []
        self.sectorWithSpace = 0
        self.file_system = root

    def save_program(self, program, path, file_name):
        psize = 0
        i = 0
        data = Data(program.program_name)
        instructions_of_program = program.get_instructions()
        while psize < instructions_of_program.__len__():
            self.generate_block(data, instructions_of_program[i:(i + 10)])
            psize += 10
            i += 10
        folder_to_save = self.file_system.cd(path)
        folder_to_save.add_new_file(file_name)

    def generate_block(self, data, instructions):
        block = BlockHdd(data.program_name)
        backuplist = instructions
        for i in backuplist:
            block.add_instruction(i)
        block.check_size()
        index_of_block = self.add_to_sector(block)
        data.save_data(self.sectorWithSpace, index_of_block)

    def add_to_sector(self, block):
        if self.blocks.__len__() == 10:
            self.sectorWithSpace += 1
            self.blocks = []
        self.blocks.append(block)
        self.sectors[self.sectorWithSpace] = self.blocks
        return self.blocks.index(block)

    def seek_program(self, command):
        for i in self.programs:
            print (i.get_program_name())
            if i.get_program_name() == command:
                return i
                # throw Program_not_found_exception
