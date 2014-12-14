from SchStrategy import SchStrategy
__author__ = 'Pato'


class SchPriority(SchStrategy):

    '''def __init__(self):
        super(SchPriority, self).__init__()
    '''
    def push_to_queue(self, sts, pcb):
        self.priority_push(sts, pcb)
        sts.ask_cpu_for_space()

    def priority_push(self, sts, pcb):
        last_index = sts.ready_queue.__len__() - 1
        if sts.ready_queue.__len__() != 0:  # Si la lista tiene elementos busca la posicion en donde insertar el pcb
            if sts.ready_queue[last_index].priority > pcb.priority:
                sts.ready_queue.append(pcb)
            else:
                for i in sts.ready_queue:
                    if i.priority < pcb.priority:
                        index_of_i = sts.ready_queue.index(i)
                        sts.ready_queue.insert(index_of_i, pcb)
                        break
        else:
            sts.ready_queue.append(pcb)
