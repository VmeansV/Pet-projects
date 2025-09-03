from collections import OrderedDict

def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    my_dict = OrderedDict()
    my_dict['name'] = grades['name']
    my_dict['top_grade'] = max(grades['grades'])
    return dict(my_dict)