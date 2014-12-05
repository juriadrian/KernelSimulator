__author__ = 'adri'


class Data():

    def __init__(self, program_name):
        self.program_name = program_name
        self.actual_key = None
        self.data = {} #Dictionary where the key is the sector in the hard disk and the value is in which block is allocated the instruction
        #Inicializacion de un diccionario por david => dict(zip(range(0, 9), [None] * 10))

    def save_data(self, key, value):
        if key != self.actual_key:
            self.data[key] = []
            self.actual_key = key
        self.data[key].append(value)