from FileSys.Data import Data
from Handlers.BlockHdd import BlockHdd

__author__ = 'Pato'


class HardDisk:

    def __init__(self):
        self.sectors = {}
        self.blocks = []
        self.sectorWithSpace = 0
        self.file_system = Folder('root')

    def save_program(self, program, folder_name, file_name):
        psize = 0
        i = 0
        data = Data(program.program_name)
        while psize < program.get_instructions().size():
            self.generate_block(data, program.get_instructions[i:(i + 10)])
            psize += 10
            i += 10
        self.file_system.add_file_to_folder(folder_name, file_name, data)

    def generate_block(self, data, program_name, instructions):
        block = BlockHdd(program_name)
        backuplist = instructions()
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
