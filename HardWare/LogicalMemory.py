from numpy.core.defchararray import index
from HardWare import FirstFit
from HardWare.MemoryBlock import MemoryBlock

__author__ = 'adri'

# Mirar como se modifican los bloques libres
class LogicalMemory:

    def __init__(self, memory, hdd):
        self.memory = memory
        self.size_of_memory = self.memory.size_of_memory
        self.empty_blocks = []
        self.set_empty_blocks()
        self.used_blocks = []
        self.fit = FirstFit()
        self.hdd = hdd

    def set_empty_blocks(self):
        memory_block = MemoryBlock(0, self.size_of_memory())
        self.empty_blocks.append(memory_block)

    def write_program(self, pcb):
        number_of_instructions = pcb.size_of_program
        empty_block = self.check_for_empty_blocks(number_of_instructions)
        self.write_program_in_block(empty_block, pcb)
        self.modify_blocks(empty_block, number_of_instructions)

    def modify_blocks(self, empty_block, number_of_instructions):
        modified_index = empty_block.init + number_of_instructions
        new_used_block = MemoryBlock(empty_block.init, modified_index)
        self.used_blocks.append(new_used_block)
        if modified_index == empty_block.end:
            self.empty_blocks.remove(empty_block)
        else:
            empty_block.change_init(modified_index)

    def check_for_empty_blocks(self, number_of_instructions):
        return self.fit.get_an_empty_block(self.empty_blocks, number_of_instructions)

    def write_program_in_block(self, empty_block, pcb):
        list_of_hdd_block = self.get_hdd_blocks(pcb)
        self.write_blocks_on_memory(empty_block, list_of_hdd_block)

    def get_hdd_blocks(self, pcb):
        data = pcb.data.data
        hdd_sectors = self.hdd.sectors
        list_of_hdd_blocks = []
        for sector, blocks in data.iteritems():
            program_blocks = hdd_sectors[sector]
            corrected_blocks = self.get_corrected_blocks(program_blocks, blocks)
            list_of_hdd_blocks += corrected_blocks
        return list_of_hdd_blocks

    def get_corrected_blocks(self, program_blocks, blocks):
        corrected_blocks = list(filter(lambda x: x.__index__() in blocks, program_blocks))
        return corrected_blocks

    def write_one_block_on_memory(self, hdd_block, empty_block):
        actual_index_of_memory = empty_block.init
        for i in hdd_block:
            self.memory[actual_index_of_memory] = i
            actual_index_of_memory += 1

    def write_blocks_on_memory(self, empty_block, list_of_hdd_block):
        for b in list_of_hdd_block:
            self.write_one_block_on_memory(b, empty_block)




