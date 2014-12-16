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
        self.id = 0
        self.set_empty_blocks()
        self.hdd = hdd
        self.memory_management = ContiguousMemoryAllocation()

    def set_empty_blocks(self):
        memory_block = MemoryBlock(0, self.size_of_memory, self.id)
        self.id += 1
        self.empty_blocks.append(memory_block)

    def write_program(self, pcb):
        self.memory_management.write_program(pcb, self)

    def delete_program(self, pcb):
        self.memory_management.delete_program(pcb, self)

    def swap_block(self, block):
        self.used_blocks.remove(block)
        self.empty_blocks.append(block)

    def compaction(self):
        self.memory_management.compaction(self)









