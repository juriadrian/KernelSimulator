__author__ = 'adri'

from PcbHandler import PcbHandler


class HandlerTimeOut (PcbHandler):

    def __init__(self, pcb):
        self.pcb = pcb

    def execute(self, a_kernel):
        a_kernel.my_short_scheduler.push_to_queue(self.pcb)
        a_kernel.my_short_scheduler.ask_cpu_for_space()
