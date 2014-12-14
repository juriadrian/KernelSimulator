import unittest
from HardWare.HardDisk import HardDisk
from HardWare.Memory import Memory
from Handlers.Loader import Loader
from Handlers.LongTermScheduler import LongTermScheduler
from Kernel.Kernel import Kernel
__author__ = 'Angeles'

class KernelTest(unittest.TestCase):
    def setUp(self):
        hdd = HardDisk()
        memory = Memory()
        long = LongTermScheduler()
        loader = Loader()
        kernel = Kernel(memory, hdd, long, loader)

