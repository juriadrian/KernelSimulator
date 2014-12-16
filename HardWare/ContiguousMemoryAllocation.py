from HardWare.Fit import FirstFit
from HardWare.MemoryBlock import MemoryBlock
from HardWare.MemoryManagement import MemoryManagement

__author__ = 'adri'


class ContiguousMemoryAllocation(MemoryManagement):

    def __init__(self):
        self.fit = FirstFit()

    def write_program(self, pcb, logical_memory):
        number_of_instructions = pcb.size_of_program
        empty_block = self.check_for_empty_blocks(number_of_instructions, logical_memory)
        self.write_program_in_block(empty_block, pcb, logical_memory)
        self.modify_blocks(empty_block, number_of_instructions, logical_memory, pcb)

    def check_for_empty_blocks(self, number_of_instructions, logical_memory):
        return self.fit.get_an_empty_block(logical_memory.empty_blocks, number_of_instructions)

    def modify_blocks(self, empty_block, number_of_instructions, logical_memory, pcb):
        modified_index = empty_block.init + number_of_instructions
        new_used_block = MemoryBlock(empty_block.init, modified_index, logical_memory.id)
        pcb.set_id(new_used_block.id)
        logical_memory.id += 1
        logical_memory.used_blocks.append(new_used_block)
        if modified_index == empty_block.end:
            logical_memory.empty_blocks.remove(empty_block)
        else:
            empty_block.change_init(modified_index)

    def write_program_in_block(self, empty_block, pcb, logical_memory):
        list_of_hdd_block = self.get_hdd_blocks(pcb, logical_memory)
        self.write_blocks_on_memory(empty_block, list_of_hdd_block, logical_memory)

    def get_hdd_blocks(self, pcb, logical_memory):
        data = pcb.data.blocks
        hdd_sectors = logical_memory.hdd.sectors
        list_of_hdd_blocks = []
        for sector, blocks in data.iteritems():
            program_blocks = hdd_sectors[sector]
            corrected_blocks = self.get_corrected_blocks(program_blocks, blocks)
            list_of_hdd_blocks += corrected_blocks
        return list_of_hdd_blocks

    def get_corrected_blocks(self, program_blocks, blocks):
        corrected_blocks = list(filter(lambda x: program_blocks.index(x) in blocks, program_blocks))
        return corrected_blocks

    def write_one_block_on_memory(self, hdd_block, empty_block, logical_memory):
        actual_index_of_memory = empty_block.init
        for i in hdd_block.instructions:
            logical_memory.memory.cells[actual_index_of_memory] = i
            actual_index_of_memory += 1

    def write_blocks_on_memory(self, empty_block, list_of_hdd_block, logical_memory):
        for b in list_of_hdd_block:
            self.write_one_block_on_memory(b, empty_block, logical_memory)

    def compaction(self, logical_memory):
        sorted_used_blocks = sorted(logical_memory.used_blocks, key=(lambda block: block.init))
        new_index = 0
        for b in sorted_used_blocks:
            if b.init != new_index:
                self.move_block(b, new_index, logical_memory)
            new_index = b.end
        new_empty_block = MemoryBlock(sorted_used_blocks[-1].end + 1, logical_memory.memory.size_of_memory, logical_memory.id)
        logical_memory.id += 1
        logical_memory.empty_blocks = [new_empty_block]

    def move_block(self, block, new_index, logical_memory):
        old_memory_index = block.init
        new_memory_index = new_index
        i = block.end - block.init
        block.init = new_index
        block.end = new_index + i
        while i > 0:
            logical_memory.memory.change_instruction_cell(old_memory_index, new_memory_index)
            new_memory_index += 1
            old_memory_index += 1
            i -= 1

    def delete_program(self, pcb, logical_memory):
        block_id = pcb.block_id
        block = next(x for x in logical_memory.used_blocks if x.id == block_id)
        index = block.init
        while index < block.end:
            logical_memory.memory.cells[index] = None
            index += 1
        logical_memory.swap_block(block)

    def get_instruction_of_cell(self, pc, block_id, logical_memory):
        block = next(x for x in logical_memory.used_blocks if x.id == block_id)
        return logical_memory.memory.get_instruction_of_cell(block.init + pc)