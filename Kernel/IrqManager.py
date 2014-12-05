__author__ = 'adri'

class IrqManager:

    def __init__(self, a_kernel):
        self.pending_irqs = []
        self.kernel = a_kernel

    def handle(self, irq):
        self.pending_irqs.append(irq)

    def execute(self):
        for irq in self.pending_irqs:
            irq.execute(self.kernel)
            self.pending_irqs.remove(irq)