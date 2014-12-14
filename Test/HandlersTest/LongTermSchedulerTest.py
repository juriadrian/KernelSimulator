from FileSys.File import Data
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from Handlers.ShortTermScheduler import ShortTermScheduler
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
import unittest


class LongTermSchedulerTest(unittest.TestCase):

    def setUp(self):
        self.console = ConsoleOutput()
        self.inst = Instruction('h', self.console)
        self.program = Program('testP')
        self.program.add_instruction(self.inst)
        self.hdd = HardDisk()
        self.loader = Loader()
        self.irqManager = IrqManager()
        self.memory = Memory()
        self.long = LongTermScheduler()
        self.kernel = Kernel(self.memory, self.hdd, self.long, self.loader)
        self.kernel.my_irq_manager = self.irqManager
        self.cpu = CpuModel(self.kernel, self.memory, self.irqManager)
        self.kernel.my_short_scheduler.set_cpu(self.cpu)
        self.data = Data('testP', 1)
        self.pcb1 = PCB(0, self.data)
        self.pcb2 = PCB(1, self.data)

    def handle_pcb_empty_cpu_test(self):
        self.long.handle_pcb(self.pcb2, self.kernel.my_short_scheduler)
        self.assertEqual(self.long.waiting_queue.__len__(), 0)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__len__(), 0)
        self.assertEqual(self.cpu.pcb, self.pcb2)

    def handle_pcb_used_cpu_test(self):
        self.cpu.change_pcb(self.pcb1)
        self.long.handle_pcb(self.pcb2, self.kernel.my_short_scheduler)
        self.assertEqual(self.long.waiting_queue.__len__(), 0)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__len__(), 1)
        self.assertEqual(self.cpu.pcb, self.pcb1)