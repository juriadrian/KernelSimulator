from Handlers.SchPriority import SchPriority
from Handlers.SchRoundRobin import SchRoundRobin
from HardWare.CpuModel import CpuModel
from SchFifo import SchFifo


class ShortTermScheduler:

    def __init__(self, kernel, sch_strategy=SchFifo(), q=-1):
        self.kernel = kernel
        self.quantum = q
        self.ready_queue = []
        self.ready_queue_size = 50
        self.sch_strategy = sch_strategy
        self.cpu = None

    def set_cpu(self, cpu):
        self.cpu = cpu

    def not_full(self):
        return self.ready_queue_size > self.ready_queue.__len__()

    def push_to_queue(self, pcb):
        if self.not_full():
            self.sch_strategy.push_to_queue(self, pcb)

    def send_next_to_cpu(self):
        self.sch_strategy.send_next_to_cpu(self)
        self.kernel.my_long_scheduler.send_pcb_to_sts(self)
        self.increase_pcbs_priority(1)

    def ask_cpu_for_space(self):
        if self.cpu.pcb is None:
            self.send_next_to_cpu()

    def set_priority_strategy(self):
        self.sch_strategy = SchPriority()
        self.quantum = -1

    def set_round_robin_strategy(self, quantum, strategy=SchFifo()):
        self.sch_strategy = SchRoundRobin(strategy)
        self.quantum = quantum

    def increase_pcbs_priority(self, y):
        self.ready_queue = map((lambda x: x.increase_priority(y)), self.ready_queue)