from HardWare import FirstFit
from HardWare.MemoryBlock import MemoryBlock

__author__ = 'adri'


class LogicalMemory:

    def __init__(self, memory):
        self.memory = memory
        self.size_of_memory = self.memory.size_of_memory
        self.empty_blocks = []
        self.set_empty_blocks()
        self.used_blocks = []
        self.fit = FirstFit()

    def set_empty_blocks(self):
        memory_block = MemoryBlock(0, self.size_of_memory())
        self.empty_blocks.append(memory_block)

    def write_program(self, pcb):
        number_of_instructions = pcb.total_instructions()
        empty_block = self.check_for_empty_blocks(number_of_instructions)
        self.write_program_in_block(empty_block, pcb)

    def check_for_empty_blocks(self, number_of_instructions):
        return self.fit.get_an_empty_block(self.empty_blocks, number_of_instructions)

    def write_program_in_block(self, empty_block, pcb):
        list_of_hdd_block = self.get_hdd_blocks(pcb)
        self.write_blocks_on_memory(empty_block, list_of_hdd_block)

    def get_hdd_blocks(self, pcb):
        data = pcb.data.data



    def write_blocks_on_memory(self, empty_block, list_of_hdd_block):
        for b in list_of_hdd_block:
            self.write_one_block_on_memory(b, empty_block)

    def write_one_block_on_memory(self, hdd_block, empty_block):
        actual_index_of_memory = empty_block.init
        for i in hdd_block:
            self.memory[actual_index_of_memory] = i
            actual_index_of_memory += 1




