import unittest
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from HardWare.CpuModel import CpuModel
from HardWare.HardDisk import HardDisk
from HardWare.Memory import Memory
from Kernel.Instruction import Instruction
from Kernel.Kernel import Kernel
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput

__author__ = 'adri'


class ContiguousMemoryAllocation(unittest.TestCase):

    def setUp(self):
        self.console = ConsoleOutput()
        self.inst = Instruction('h', self.console)
        self.program = Program('testP')
        self.program.add_instruction(self.inst)
        self.hdd = HardDisk()
        self.file_system = self.hdd.file_system
        self.memory = Memory()
        self.long = LongTermScheduler()
        self.loader = Loader()
        self.kernel = Kernel(self.memory, self.hdd, self.long, self.loader)
        self.irq_manager = self.kernel.my_irq_manager
        self.cpu = CpuModel(self.kernel, self.memory, self.irq_manager)
        self.kernel.my_short_scheduler.set_cpu(self.cpu)
        self.logical_memory = self.kernel.logical_memory

    def write_program_test(self):
        self.logical_memory.write_program()