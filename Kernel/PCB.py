__author__ = 'Pato'


class PCB:

    def __init__(self, mempos, pid, priority):
        self.pid = pid
        ##self.programState = Ready() arranca en New()
        self.memory_position = mempos
        self.pc = 0
        self.priority = priority

    def increase_priority(self, x):
        self.priority += x

    #POR AHORA NO CREE LOS STATES, PORQUE NO HAY DIFERENCIA ENTRE EL DISENIO QUE TENEMOS
    #Y LO QUE DEBERIAN HACER SUS ESTADOS