from HardWare.Fit import Fit

__author__ = 'adri'


class FirstFit(Fit):

    def get_an_empty_block(self, empty_blocks, number_of_instructions):
        first_block = None
        for b in empty_blocks:
            if b.get_size() >= number_of_instructions:
                first_block = b
                break
        return first_block