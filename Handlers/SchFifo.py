from SchStrategy import SchStrategy


class SchFifo (SchStrategy):

    def push_to_queue(self, sts, pcb):
        sts.ready_queue.append(pcb)
        sts.ask_cpu_for_space()
