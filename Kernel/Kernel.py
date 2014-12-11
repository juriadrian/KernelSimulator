from Handlers.ShortTermScheduler import ShortTermScheduler
from HardWare.LogicalMemory import LogicalMemory
from IrqManager import IrqManager

__author__ = 'Pato'

from PCB import PCB
from Handlers.HandlerNew import HandlerNew


class Kernel:

    def __init__(self, a_memory, a_disk, a_long_scheduler, a_loader):
        self.pcb_instruction =[]
        self.my_hard_disk = a_disk
        self.my_memory = a_memory
        self.logical_memory = LogicalMemory(self.my_memory, self.my_hard_disk)
        self.pid = 1
        self.my_long_scheduler = a_long_scheduler
        self.my_short_scheduler = ShortTermScheduler(self)
        self.my_loader = a_loader
        self.my_irq_manager = IrqManager(self)

    '''def run(self, command):
        memory_position = self.my_loader.run(command, self.my_hard_disk, self.my_memory)
        self.create_pcb(memory_position)'''

    def create_file_system(self):
        i_nodes = self.my_hard_disk.i_nodes


    def run(self, pcb):
        self.my_loader.run(pcb, self.logical_memory)
        self.my_irq_manager.


    def create_pcb(self, memory_position):
        #Crear un nuemero random para la prioridad del pcb
        pcb = PCB(memory_position, self.pid, 5)
        self.my_irq_manager.handle(HandlerNew(pcb))
        self.pid += 1