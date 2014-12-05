__author__ = 'adri'

from PcbHandler import PcbHandler


class HandlerNew(PcbHandler):

    def __init__(self, a_pcb):
        self.pcb = a_pcb

    def execute(self, a_kernel):
        a_kernel.my_long_scheduler.handle_pcb(self.pcb, a_kernel.my_short_scheduler)
        a_kernel.my_short_scheduler.ask_cpu_for_space()