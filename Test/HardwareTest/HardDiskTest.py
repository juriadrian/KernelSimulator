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
        #self.hdd = HardDisk([self.program])
        self.hdd = HardDisk()
        
    def test_seek_program(self):
        program_founded = self.hdd.seek_program('testP')
        self.assertEqual(program_founded, self.program)

    def test_save_program(self):
        self.hdd.save_program(self.program)
        self.assertEqual(len(self.hdd.programs), 2)

    def test_split_into_two(self):
        l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24.25]
        h = self.hdd.split_into_two(l)
        self.assertEqual(h.__getitem__(0), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(h.__getitem__(1), [11,12,13,14,15,16,17,18,19,20,21,22,23,24.25])