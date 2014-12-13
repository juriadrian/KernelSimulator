__author__ = 'adri'

class IrqManager:

    def __init__(self):
        self.pending_irqs = []

    def handle(self, irq):
        self.pending_irqs.append(irq)

    def execute(self):
        map(lambda x: x.execute, self.pending_irqs)
        self.pending_irqs = []