import unittest
from Handlers.HandlerEof import HandlerEof
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from HardWare.CpuModel import CpuModel
from HardWare.HardDisk import HardDisk
from HardWare.Memory import Memory
from Kernel.Instruction import Instruction
from Kernel.IrqManager import IrqManager
from Kernel.Kernel import Kernel
from Kernel.PCB import PCB
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput

__author__ = 'adri'


class HandlerEofTest(unittest.TestCase):

    def setUp(self):
        self.console = ConsoleOutput()
        self.inst = Instruction('h', self.console)
        self.program = Program('testP')
        self.program.add_instruction(self.inst)
        self.hdd = HardDisk([self.program])
        self.memory = Memory()
        self.long = LongTermScheduler()
        self.loader = Loader()
        self.irqManager = IrqManager()
        self.kernel = Kernel(self.memory, self.hdd, self.long, self.loader, self.irqManager)
        self.cpu = CpuModel(self.kernel, self.memory, self.irqManager)
        self.kernel.my_short_scheduler.set_cpu(self.cpu)
        self.pcb1 = PCB(0, 5, 7)
        self.eof = HandlerEof(self.pcb1)

    def execute_test(self):
        self.eof.execute(self.kernel)
        self.assertEqual(3, 3)