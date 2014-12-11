__author__ = 'Pato'


class PCB:

    def __init__(self, pid, data, priority=-1):
        self.pid = pid
        #self.programState = Ready() arranca en New()
        self.pc = 0
        self.data = data
        self.size_of_program = data.size
        self.priority = priority

    def increase_priority(self, x):
        self.priority += x

    #POR AHORA NO CREE LOS STATES, PORQUE NO HAY DIFERENCIA ENTRE EL DISENIO QUE TENEMOS
    #Y LO QUE DEBERIAN HACER SUS ESTADOS