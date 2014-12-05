__author__ = 'Pato'


class Loader:

    def __init__(self):
        pass

    def run(self, a_command, a_hard_disk, a_memory):
        program_on_disk = a_hard_disk.seek_program(a_command)
        memory_position = a_memory.write_program(program_on_disk)
        return memory_position

    def remove(self, pcb):
        pass