import unittest
from FileSys.File import Data
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from HardWare.CpuModel import CpuModel
from HardWare.HardDisk import HardDisk
from HardWare.Memory import Memory
from Kernel.Instruction import Instruction
from Kernel.Kernel import Kernel
from Kernel.PCB import PCB
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput

__author__ = 'adri'


class ContiguousMemoryAllocation(unittest.TestCase):

    def setUp(self):
        self.console = ConsoleOutput()

        self.inst = Instruction('h', self.console)
        self.program = Program('testP')
        self.program.add_instruction(self.inst)

        self.inst2 = Instruction('h2', self.console)
        self.program2 = Program('testP2')
        self.program2.add_instruction(self.inst2)

        self.inst3 = Instruction('h3', self.console)
        self.program3 = Program('testP3')
        self.program3.add_instruction(self.inst3)

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
        self.hdd.save_program(self.program, '/', 'testP')
        data = Data('testP', 1)
        data.save_data(0, 0)
        pcb = PCB(1, data)
        self.logical_memory.write_program(pcb)
        self.assertEqual(self.memory.cells[0], self.inst)
        self.assertEqual(self.memory.cells[1], 'EOF')

    def compaction_test(self):
        self.hdd.save_program(self.program, '/', 'testP')
        self.hdd.save_program(self.program2, '/', 'testP2')
        self.hdd.save_program(self.program3, '/', 'testP3')
        pcb1 = PCB(0, self.file_system.get_data('testP'))
        pcb2 = PCB(1, self.file_system.get_data('testP2'))
        pcb3 = PCB(2, self.file_system.get_data('testP3'))
        self.logical_memory.write_program(pcb1)
        self.logical_memory.write_program(pcb2)
        self.logical_memory.write_program(pcb3)

        self.assertEqual(self.memory.cells[0], self.inst)
        self.assertEqual(self.memory.cells[1], 'EOF')
        self.assertEqual(self.memory.cells[2], self.inst2)
        self.assertEqual(self.memory.cells[3], 'EOF')
        self.assertEqual(self.memory.cells[4], self.inst3)
        self.assertEqual(self.memory.cells[5], 'EOF')

        self.logical_memory.delete_program(pcb2)

        self.assertEqual(self.memory.cells[0], self.inst)
        self.assertEqual(self.memory.cells[1], 'EOF')
        self.assertEqual(self.memory.cells[2], None)
        self.assertEqual(self.memory.cells[3], None)
        self.assertEqual(self.memory.cells[4], self.inst3)
        self.assertEqual(self.memory.cells[5], 'EOF')

        self.logical_memory.compaction()

        self.assertEqual(self.memory.cells[0], self.inst)
        self.assertEqual(self.memory.cells[1], 'EOF')
        self.assertEqual(self.memory.cells[2], self.inst3)
        self.assertEqual(self.memory.cells[3], 'EOF')
        self.assertEqual(self.memory.cells[4], None)
        self.assertEqual(self.memory.cells[5], None)









