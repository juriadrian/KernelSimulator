__author__ = 'adri'

from PcbHandler import PcbHandler


class HandlerEof(PcbHandler):

    def __init__(self, a_pcb):
        self.pcb = a_pcb

    def execute(self, a_kernel):
        a_kernel.my_loader.remove(self.pcb)
        a_kernel.my_short_scheduler.ask_cpu_for_space()