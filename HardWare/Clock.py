__author__ = 'adri'
import threading
import time


class Clock(threading.Thread):

    def __init__(self, aDelayInSeconds = 1, aNumberOfHits = -1):
        threading.Thread.__init__(self)
        self.listeners = []
        self.delayInSeconds = aDelayInSeconds
        self.numberOfHits = aNumberOfHits

    def run(self):
        currentHit = 1
        while(self.numberOfHits < 0 or self.numberOfHits >= currentHit):
            currentHit = currentHit +1
            time.sleep(self.delayInSeconds)

            self.notify()

    def register(self, listener):
        self.listeners.append(listener)

    def notify(self):
        for listener in self.listeners:
            listener()
'''
class Example:

    def __init__(self):
        self.index = 0

    def execute(self):
        self.index = self.index +1
        print(self.index)

class cpu:
    init(irqManager)

    fetcInt:
            ....irqManager.Hanldle(kill)

class IrqManager:

    def __init__(self):
        self.pendingIrqs = []

    def handle(self, irq):

        self.pendingIrqs.append(irq)

    def execute(self):
        for irq in self.pendingIrqs:
            ...
irqManager = irqManager
cpu = Cpu(irqManager)
clock = Clock(aNumberOfHits=3)
clock.register(cpu.execute)
clock.start()

time.sleep(5)
'''
