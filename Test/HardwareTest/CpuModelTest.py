import unittest
from FileSys.File import Data
from FileSys.Folder import Folder
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
        self.hdd = HardDisk()
        self.loader = Loader()
        self.irqManager = IrqManager()
        self.memory = Memory()
        self.long = LongTermScheduler()
        self.kernel = Kernel(self.memory, self.hdd, self.long, self.loader)
        self.kernel.my_irq_manager = self.irqManager
        self.cpu = CpuModel(self.kernel, self.memory, self.irqManager)
        self.short = self.kernel.my_short_scheduler
        self.short.set_cpu(self.cpu)
        self.data = Data('Program_under_test', 1)
        self.pcb1 = PCB(0, self.data)
        self.pcb2 = PCB(1, self.data)
        self.pcb3 = PCB(2, self.data)
        self.pcb4 = PCB(3, self.data)

    def change_pcb_test(self):
        self.assertEqual(self.cpu.pcb, None)
        self.cpu.change_pcb(self.pcb2)
        self.assertEqual(self.cpu.pcb, self.pcb2)

    def execute_test(self):# Error: AttributeError: 'list' object has no attribute 'size'
        self.assertEqual(self.console.get_collection().__len__(), 0)
        self.hdd.save_program(self.program, '/', 'Program_under_test')
        self.kernel.run('Program_under_test')
        self.irqManager.execute()
        self.cpu.execute()
        self.assertEqual(self.console.get_collection().__len__(), 1)

