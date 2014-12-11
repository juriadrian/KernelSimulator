from HardWare.Memory import Memory
from Kernel.Instruction import Instruction
from Kernel.PCB import PCB
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput
from Handlers.HandlerEof import HandlerEof
from Handlers.HandlerIO import HandlerIO
from Handlers.HandlerTimeOut import HandlerTimeOut

__author__ = 'Adri'


class CpuModel:

    def __init__(self, kernel, memo, im):
        self.kernel = kernel
        self.memory = memo
        self.irq_manager = im
        self.pcb = None
        self.quantum = self.kernel.my_short_scheduler.quantum

    def change_pcb(self, pcb):
        self.pcb = pcb

    def execute(self):
        count = self.quantum
        pcb_hand = None
        while count > 0 or self.quantum == -1:
            instruction = self.memory.get_instruction_of_cell(self.pcb.memory_position)#En vez de usar memory position usaremos el PROGRAM COUNTER
            if instruction == 'EOF':
                #setState con enum
                print('termino el proceso')
                pcb_hand = HandlerEof(self.pcb)
                break
            elif instruction.is_input_output():
                print('i/o')
                pcb_hand = HandlerIO(self.pcb, instruction)
                break
            else:
                count -= 1
                self.pcb.memory_position += 1
                instruction.execute()
        if pcb_hand is None:
            pcb_hand = HandlerTimeOut(self.pcb)
        self.irq_manager.handle(pcb_hand)
        self.pcb = None
