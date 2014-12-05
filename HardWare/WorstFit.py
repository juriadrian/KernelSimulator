from HardWare.Fit import Fit

__author__ = 'adri'


class WorstFit(Fit):

    def get_an_empty_block(self, empty_blocks, number_of_instructions):
        list_of_empty_blocks = filter(lambda x: x.get_size() >= number_of_instructions, empty_blocks)
        sorted_list = sorted(list_of_empty_blocks, key=(lambda x: x.get_size()), reverse=True)
        return sorted_list[0]
