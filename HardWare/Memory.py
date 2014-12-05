__author__ = 'Pato'

class Memory:

    def __init__ (self):
        self.cells = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.next_cell = 0

    def write_program(self, a_program):
        memory_position = self.next_cell
        for i in a_program.instructions:
            self.cells[self.next_cell] = i
            self.next_cell += 1
        #self.cells[self.next_cell] #NO SE QUE HACE ESTO ACA, PARA MI ES UNA LINEA DE MAS
        return memory_position

    def read(self):
        pass

    def get_instruction_of_cell(self, index):
        return self.cells.__getitem__(index)

#HAY QUE CAMBIAR LA FORMA EN LA QUE SE ESCRIBE UN PROGRAMA EN MEMORIA, USANDO EL EOF (END OF FILE)