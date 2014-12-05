__author__ = 'Pato'


class Instruction:

    ##TIENE QUE DECIR EL TIPO DE INSTRUCCION QUE ES, SI ES PARA UN DISPOSITIVO I/O O PARA EL CPU
    ## SI ES DE I/O TIENE QUE DECIR EL DISPOSITIVO AL QUE TIENE QUE IR

    def __init__(self, instruction, a_console, is_input_output = False, a_device = None):
        self.what_to_do = instruction
        self.myconsole = a_console
        self.input_output = is_input_output
        self.device = a_device

    def execute(self):
        self.myconsole.print_in_console(self.get_what_to_do())

    def get_what_to_do(self):
        return self.what_to_do

    def is_input_output(self):
        return self.input_output

    def get_device(self):
        return self.device
