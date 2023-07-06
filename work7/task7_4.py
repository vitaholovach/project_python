def max(value_iterable):
    max_value = value_iterable[0]
    for value in value_iterable:
        if value > max_value:
            max_value = value
    return max_value


def min(value_iterable):
    min_value = value_iterable[0]
    for value in value_iterable:
        if value < min_value:
            min_value = value
    return min_value
