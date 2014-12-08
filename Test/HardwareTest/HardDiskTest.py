from FileSys.Folder import Folder
from Kernel.Instruction import Instruction
from HardWare.HardDisk import HardDisk
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
        self.file_system = Folder('root')
        self.hdd = HardDisk(self.file_system)
        
    def seek_program_test(self):
        program_founded = self.hdd.seek_program('testP')
        self.assertEqual(program_founded, self.program)

    def save_program_test(self):
        self.hdd.save_program(self.program, '/', 'prueba1')
        blocks = self.hdd.sectors[0]
        block = blocks[0]
        instruction = block.instructions[0]
        self.assertEqual(instruction, self.inst)