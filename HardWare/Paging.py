from HardWare.MemoryManagement import MemoryManagement

__author__ = 'adri'


class Paging(MemoryManagement):

    def __init__(self):
        self.empty_pages = []
        self.used_pages

    def write_program(self, pcb, logical_memory):
        pages = logical_memory.get_hdd_blocks()
        if len(self.empty_pages) > total_pages:
            memory_frames = self.get_memory_frames(total_pages)
            for f in memory_frames:
                self.write_page_on_frame(f, pages.pop(0))