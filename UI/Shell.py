__author__ = 'Pato'

class My_shell:
    def __init__(self, my_kernel):
        self.my_kernel = my_kernel

    def read_instruction(self, comand):
        self.my_kernel.run(comand)