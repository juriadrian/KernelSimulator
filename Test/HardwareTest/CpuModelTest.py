import unittest
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


class CpuModelTest(unittest.TestCase):
    
    def setUp(self):
        self.console = ConsoleOutput()
        self.inst = Instruction('instruction_number_1', self.console)
        self.program = Program('Program_under_test')
        self.program.add_instruction(self.inst)
        self.hdd = HardDisk([self.program])
        self.loader = Loader()
        self.memory = Memory()
        self.long = LongTermScheduler()
        self.kernel = Kernel(self.memory, self.hdd, self.long, self.loader)
        self.irq_manager = self.kernel.my_irq_manager
        self.cpu = CpuModel(self.kernel, self.memory, self.irq_manager)
        self.short = self.kernel.my_short_scheduler
        self.short.set_cpu(self.cpu)
        self.pcb1 = PCB(0, 5, 7)
        self.pcb2 = PCB(1, 6, 2)
        self.pcb3 = PCB(2, 7, 4)
        self.pcb4 = PCB(3, 8, 1)

    def change_pcb_test(self):
        self.assertEqual(self.cpu.pcb, None)
        self.cpu.change_pcb(self.pcb2)
        self.assertEqual(self.cpu.pcb, self.pcb2)

    def execute_test(self):
        self.assertEqual(self.console.get_collection().__len__(), 0)
        self.hdd.save_program(self.program)
        self.kernel.run('Program_under_test')
        self.irq_manager.execute()
        self.cpu.execute()
        self.assertEqual(self.console.get_collection().__len__(), 1)

