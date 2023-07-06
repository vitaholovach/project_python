from typing import Callable, Iterable, Any


def option_filter(callback: Callable[[Any], bool], sequence: Iterable[Any]):
    filtered_list = []
    for item in sequence:
        if callback(item):
            filtered_list.append(item)
    return filtered_list
