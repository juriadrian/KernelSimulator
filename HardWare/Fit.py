__author__ = 'adri'
'''Fit is the super class of the strategies: First-fit Best-fit and Worst-fit'''


class Fit:

    def __init__(self):
        pass

    def get_an_empty_block(self, empty_blocks, number_of_instructions):
        pass


class FirstFit(Fit):

    def get_an_empty_block(self, empty_blocks, number_of_instructions):
        first_block = next(x for x in empty_blocks if x.get_size >= number_of_instructions)
        return first_block


class BestFit(Fit):

    def get_an_empty_block(self, empty_blocks, number_of_instructions):
        list_of_empty_blocks = filter(lambda x: x.get_size() >= number_of_instructions, empty_blocks)
        sorted_list = sorted(list_of_empty_blocks, key=(lambda x: x.get_size()))
        return sorted_list[0]


class WorstFit(Fit):

    def get_an_empty_block(self, empty_blocks, number_of_instructions):
        list_of_empty_blocks = filter(lambda x: x.get_size() >= number_of_instructions, empty_blocks)
        sorted_list = sorted(list_of_empty_blocks, key=(lambda x: x.get_size()), reverse=True)
        return sorted_list[0]