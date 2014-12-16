__author__ = 'Pato'


class PCB:

    def __init__(self, pid, data, priority=-1):
        self.pid = pid
        #self.programState = Ready() arranca en New()
        self.pc = 0
        self.data = data
        self.size_of_program = data.size
        self.block_id = None
        self.priority = priority

    def increase_priority(self, x):
        self.priority += x

    def set_id(self, id):
        self.block_id = id



    #POR AHORA NO CREE LOS STATES, PORQUE NO HAY DIFERENCIA ENTRE EL DISENIO QUE TENEMOS
    #Y LO QUE DEBERIAN HACER SUS ESTADOS