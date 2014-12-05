__author__ = 'adri'

from PcbHandler import PcbHandler


class HandlerIO(PcbHandler):

    def __init__(self, pcb):
        super(HandlerIO, self).__init__(pcb)

    def execute(self, a_kernel):
        a_kernel.my_short_scheduler.send_to_io_queue(self.pcb, a_kernel.cpu)