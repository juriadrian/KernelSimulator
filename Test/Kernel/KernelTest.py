import unittest
from FileSys.Folder import Folder
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from HardWare.CpuModel import CpuModel
from HardWare.HardDisk import HardDisk
from HardWare.Memory import Memory
from Kernel.Instruction import Instruction
from Kernel.Kernel import Kernel
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput
__author__ = 'Angeles'

class KernelTest(unittest.TestCase):
    def setUp(self):
        self.console = ConsoleOutput()
        self.inst1 = Instruction('instruccion del primer programa', self.console)
        self.program1 = Program('Primer programa')
        self.program1.add_instruction(self.inst1)
        self.hdd = HardDisk()
        self.memory = Memory()
        self.long = LongTermScheduler()
        self.loader = Loader()
        self.kernel = Kernel(self.memory, self.hdd, self.long, self.loader)
        self.irq_manager = self.kernel.my_irq_manager
        self.cpu = CpuModel(self.kernel, self.memory, self.irq_manager)
        self.kernel.my_short_scheduler.set_cpu(self.cpu)
        self.documents_folder = Folder('Documents', self.hdd, self.hdd.file_system, self.hdd.file_system)
        self.hdd.file_system.add_folder(self.documents_folder)
        self.hdd.save_program(self.program1, 'Documents/', 'main.py')

    def run_test(self):
        self.kernel.run('/Documents/main.py')