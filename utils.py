def find_max(values):
    max_value = values[0]
    for x in values:
        if x > max_value:
            max_value = x
    return max_value