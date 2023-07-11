from typing import Callable, Any, Iterable


def map_option(function: Callable[[Any], Any], iterable: Iterable) -> Iterable:
    mapped_items = []
    for item in iterable:
        mapped_items.append(function(item))
    return mapped_items
