from FileSys.File import Data
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from Handlers.SchPriority import SchPriority
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


class ShortTermSchedulerTest(unittest.TestCase):

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
        self.kernel = Kernel(self.memory, self.hdd, self.long, self.loader)
        self.kernel.my_irq_manager = self.irqManager
        self.cpu = CpuModel(self.kernel, self.memory, self.irqManager)
        self.kernel.my_short_scheduler.set_cpu(self.cpu)
        self.data = Data('testP', 1)
        self.pcb1 = PCB(0, self.data)
        self.pcb2 = PCB(1, self.data)
        self.pcb3 = PCB(2, self.data)
        self.pcb4 = PCB(3, self.data)
#Tests de push to queue con diferentes strategies y cpu libre o usada

    def fifo_push_to_queue_with_free_cpu_test(self):
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__len__(), 0)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, -1)

    def fifo_push_to_queue_with_used_cpu_test(self):
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(0), self.pcb2)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(1), self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, -1)

    def priority_push_to_queue_with_free_cpu_test(self):
        self.kernel.my_short_scheduler.set_priority_strategy()
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__len__(), 0)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, -1)

    def priority_push_to_queue_with_used_cpu_test(self):
        self.pcb1.priority = 2
        self.pcb2.priority = 5
        self.pcb3.priority = 7
        self.kernel.my_short_scheduler.set_priority_strategy()
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(0), self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(1), self.pcb2)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, -1)

    def robin_with_fifo_push_to_queue_with_free_cpu_test(self):
        self.kernel.my_short_scheduler.set_round_robin_strategy(5)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__len__(), 0)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, 5)

    def robin_with_fifo_push_to_queue_with_used_cpu_test(self):
        self.kernel.my_short_scheduler.set_round_robin_strategy(5)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(0), self.pcb2)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(1), self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, 5)

    def robin_with_priority_push_to_queue_with_free_cpu_test(self):
        self.kernel.my_short_scheduler.set_round_robin_strategy(5, SchPriority())
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__len__(), 0)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, 5)

    def robin_with_priority_push_to_queue_with_used_cpu_test(self):
        self.pcb1.priority = 2
        self.pcb2.priority = 5
        self.pcb3.priority = 7
        self.kernel.my_short_scheduler.set_round_robin_strategy(5, SchPriority())
        self.kernel.my_short_scheduler.push_to_queue(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(0), self.pcb3)
        self.assertEqual(self.kernel.my_short_scheduler.ready_queue.__getitem__(1), self.pcb2)
        self.assertEqual(self.kernel.my_short_scheduler.quantum, 5)

# Test de send next to cpu con distintas strategies

    def fifo_send_next_to_cpu_with_free_cpu_test(self):
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.cpu.change_pcb(None)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb2)

    def fifo_send_next_to_cpu_with_used_cpu_test(self):
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb1)

    def priority_send_next_to_cpu_with_free_cpu_test(self):
        self.pcb1.priority = 2
        self.pcb2.priority = 5
        self.pcb3.priority = 7
        self.kernel.my_short_scheduler.set_priority_strategy()
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.cpu.change_pcb(None)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb3)

    def priority_send_next_to_cpu_with_used_cpu_test(self):
        self.kernel.my_short_scheduler.set_priority_strategy()
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb1)

    def robin_with_fifo_send_next_to_cpu_with_free_cpu_test(self):
        self.kernel.my_short_scheduler.set_round_robin_strategy(5)
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.cpu.change_pcb(None)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb2)

    def robin_with_fifo_send_next_to_cpu_with_used_cpu_test(self):
        self.kernel.my_short_scheduler.set_round_robin_strategy(5)
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb1)

    def robin_with_priority_send_next_to_cpu_with_free_cpu_test(self):
        self.pcb1.priority = 2
        self.pcb2.priority = 5
        self.pcb3.priority = 7
        self.kernel.my_short_scheduler.set_round_robin_strategy(5, SchPriority())
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.cpu.change_pcb(None)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb3)

    def robin_with_priority_send_next_to_cpu_with_used_cpu_test(self):
        self.kernel.my_short_scheduler.set_round_robin_strategy(5, SchPriority())
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.kernel.my_short_scheduler.send_next_to_cpu()
        self.assertEqual(self.cpu.pcb, self.pcb1)

    def increase_pcb_priority_test(self):
        self.pcb1.priority = 2
        self.pcb2.priority = 5
        self.pcb3.priority = 7
        self.pcb4.priority = 1
        self.kernel.my_short_scheduler.set_priority_strategy()
        self.cpu.change_pcb(self.pcb1)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb2)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb3)
        self.kernel.my_short_scheduler.push_to_queue(self.pcb4)
        self.assertEqual(self.pcb2.priority, 5)
        self.assertEqual(self.pcb3.priority, 7)
        self.assertEqual(self.pcb4.priority, 1)
        self.kernel.my_short_scheduler.increase_pcbs_priority(1)
        self.assertEqual(self.pcb2.priority, 6)
        self.assertEqual(self.pcb3.priority, 8)
        self.assertEqual(self.pcb4.priority, 2)
        #for p in self.kernel.my_short_scheduler.ready_queue:
        #    print (p.priority)