from FileSys.Data import Data
from FileSys.Folder import Folder
from FileSys.INode import INode
from Handlers.BlockHdd import BlockHdd

__author__ = 'Pato'


class HardDisk:

    def __init__(self, root):
        self.sectors = {}
        self.blocks = []
        self.i_nodes = []
        self.sectorWithSpace = 0
        self.file_system = root
        self.i_nodes.append(INode('root'))

    def save_program(self, program, path, file_name):
        psize = 0
        i = 0
        data = Data(program.program_name)
        instructions_of_program = program.get_instructions()
        while psize < instructions_of_program.__len__():
            self.generate_block(data, instructions_of_program[i:(i + 10)])
            psize += 10
            i += 10
        self.create_file(path, file_name, data)

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

    def get_inode(self, folder_to_save_name):
        #inode_to_return = list(filter(lambda x: x.name == folder_to_save_name, self.i_nodes))
        inode_to_return = next(x for x in self.i_nodes if x.name == folder_to_save_name)
        return inode_to_return

    def create_inode_for_file(self, file_name, data, folder):
        new_inode = INode(file_name)
        new_inode.add_pointer(data)
        self.i_nodes.append(new_inode)
        inode_to_change = self.get_inode(folder.name)
        inode_to_change.add_pointer(new_inode)
        return new_inode

    def create_inode_for_folder(self, inode_name, folder_name):
        folder_inode = INode(folder_name)
        current_inode = self.get_inode(inode_name)
        current_inode.add_pointer(folder_inode)
        self.i_nodes.append(folder_inode)

    def create_file(self, path, file_name, data):
        folder_to_save = self.file_system.cd(path)
        inode = self.create_inode_for_file(file_name, data, folder_to_save)
        folder_to_save.add_new_file(file_name, inode)



#MISCELLANEOUS
    def seek_program(self, command):
        for i in self.programs:
            print (i.get_program_name())
            if i.get_program_name() == command:
                return i
                # throw Program_not_found_exception