from FileSys.File import File
from FileSys.Folder import Folder
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from HardWare.Clock import Clock
from HardWare.CpuModel import CpuModel
from HardWare.HardDisk import HardDisk
from HardWare.Memory import Memory
from Kernel.Instruction import Instruction
from Kernel.IrqManager import IrqManager
from Kernel.Kernel import Kernel
from Kernel.Program import Program
from UI.ConsoleOutput import ConsoleOutput

__author__ = 'adri'


console = ConsoleOutput()
inst1 = Instruction('instruccion del primer programa', console)
inst2 = Instruction('instruccion del segundo programa', console)
program1 = Program('Primer programa')
program2 = Program('Segundo programa')
program1.add_instruction(inst1)
program2.add_instruction(inst2)
hdd = HardDisk()
memory = Memory()
long = LongTermScheduler()
loader = Loader()
kernel = Kernel(memory, hdd, long, loader)
irq_manager = kernel.my_irq_manager
cpu = CpuModel(kernel, memory, irq_manager)
kernel.my_short_scheduler.set_cpu(cpu)
file_system = Folder('root', hdd)
documents_folder = Folder('Documents', hdd, file_system, file_system)
file_system.add_folder(documents_folder)
hdd.save_program(program1, 'Documents/', 'main.py')#Instancia un File en la carpeta correspondiente
hdd.save_program(program2, 'Documents/', 'test.py')

kernel.run('/Documents/main.py')
kernel.run('/Documents/test.py')


clock = Clock()
clock.register(cpu.execute())
clock.register(irq_manager.execute())

clock.start()