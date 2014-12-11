__author__ = 'adri'

from PcbHandler import PcbHandler


class HandlerIO(PcbHandler):

    def __init__(self, pcb, instruction):
        super(HandlerIO, self).__init__(pcb)
        self.instruction = instruction

    def execute(self, a_kernel):
        a_kernel.io_manager.send_to_io_queue(self.pcb, a_kernel.cpu, self.instruction)