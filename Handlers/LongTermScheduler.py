__author__ = 'Pato'


class LongTermScheduler:

    def __init__(self):
        self.waiting_queue = []

    def send_pcb_to_sts(self, a_short_scheduler):
        if self.waiting_queue.__len__() > 0:
            first_pcb = self.waiting_queue.pop(0)  # quiero agarrar al primero
            #first_pcb.setState(new Ready()) #si la cola de waiting tiene lugar deberia pasar ahi
            #hacer el state con enum
            a_short_scheduler.push_to_queue(first_pcb)

    def handle_pcb(self, pcb, a_short_scheduler):
        self.waiting_queue.insert(0, pcb)
        if a_short_scheduler.not_full():
            self.send_pcb_to_sts(a_short_scheduler)

