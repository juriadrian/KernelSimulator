__author__ = 'adri'


class SchStrategy():

    def __init__(self):
        pass

    def push_to_queue(self, sts, pcb):
        pass

    def send_next_to_cpu(self, sts):
        if sts.cpu.pcb is None and sts.ready_queue.__len__() > 0:
            process_to_cpu = sts.ready_queue.pop(0)
            sts.cpu.change_pcb(process_to_cpu)
