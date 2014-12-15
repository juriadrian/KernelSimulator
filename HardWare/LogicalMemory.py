from HardWare.ContiguousMemoryAllocation import ContiguousMemoryAllocation
from HardWare.MemoryBlock import MemoryBlock

__author__ = 'adri'


# Mirar como se modifican los bloques libres
class LogicalMemory:

    def __init__(self, memory, hdd):
        self.memory = memory
        self.size_of_memory = self.memory.size_of_memory
        self.empty_blocks = []
        self.used_blocks = []
        self.set_empty_blocks()
        self.hdd = hdd
        self.memory_management = ContiguousMemoryAllocation()

    def set_empty_blocks(self):
        memory_block = MemoryBlock(0, self.size_of_memory)
        self.empty_blocks.append(memory_block)

    def write_program(self, pcb):
        self.memory_management.write_program(pcb, self)









