__author__ = 'Pato'


class Loader:

    def __init__(self):
        pass

    def run(self, pcb, logical_memory):
        logical_memory.write_program(pcb)

    def remove(self, pcb):
        pass