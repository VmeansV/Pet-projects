from collections import OrderedDict

def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int |float]]:
    my_dict = OrderedDict()
    for index, row in enumerate(matrix, start=1):
        my_dict[index] = row
    return dict(my_dict)