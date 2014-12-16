from HardWare.MemoryManagement import MemoryManagement

__author__ = 'adri'


class Paging(MemoryManagement):

    def __init__(self, logical_memory):
        self.empty_frames = []
        self.used_frames = []
        self.set_empty_pages()
        self.logical_memory = logical_memory

    def set_empty_pages(self):
        size_of_memory = self.logical_memory.memory.size_of_memory
        number_of_frames = size_of_memory / 10
        while number_of_frames > 0:
            new_page = Frame()

    def write_program(self, pcb, logical_memory):
        pages = logical_memory.get_hdd_blocks()
        if len(self.empty_frames) > len(pages):
            memory_frames = self.get_memory_frames(len(pages))
            for f in memory_frames:
                self.write_page_on_frame(f, pages.pop(0), logical_memory)

    def get_memory_frames(self, number_of_pages):
        return self.empty_frames[0:number_of_pages]

    def write_page_on_frame(self, frame, page, logical_memory):
        frame_index = frame.init
        instructions = page.instructions
        for i in instructions:
            logical_memory.memory.cells[frame_index] = i
            frame_index += 1
        self.used_frames.append(page)
        self.empty_frames.remove(page)