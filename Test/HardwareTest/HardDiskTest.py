from FileSys.File import Data, INode
from FileSys.Folder import Folder
from Kernel.Instruction import Instruction
from HardWare.HardDisk import HardDisk, BlockHdd
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput
import unittest

__author__ = 'adri'


class HardwareTest(unittest.TestCase):

    def setUp(self):
        self.console = ConsoleOutput()
        self.inst = Instruction('h', self.console)
        self.program = Program('testP')
        self.program.add_instruction(self.inst)
        self.hdd = HardDisk()
        self.file_system = self.hdd.file_system

    def save_program_test(self):
        self.hdd.save_program(self.program, '/', 'prueba1')
        blocks = self.hdd.sectors[0]
        block = blocks[0]
        instruction = block.instructions[0]
        self.assertEqual(instruction, self.inst)

    def generate_block_test(self):
        temp_data = Data('testP', 1)
        self.hdd.generate_block(temp_data, [self.inst])
        self.assertEqual(self.hdd.sectors[0][0].instructions[0], self.inst)
        
    def add_to_sector_test(self):
        block = BlockHdd('testP')
        index_of_block = self.hdd.add_to_sector(block)
        self.assertEqual(self.hdd.sectors[0][index_of_block], block)

    def get_inode_test(self):
        new_folder = Folder('Documents', self.hdd)
        self.file_system.add_folder(new_folder)
        self.assertEqual(self.hdd.get_inode('Documents').name, 'Documents')
