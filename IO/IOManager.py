__author__ = 'adri'


class IOManager:

    def __init__(self):
        self.printer_queue = []

    def send_to_io_queue(self, pcb, instruction):
        self.printer_queue.append(instruction)