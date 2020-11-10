def reverse_dict(dict):
    # swap keys and values within dict and return dict
    new_dict = {}
    for k, v in dict.items():
        new_dict[v] = k
    return new_dict
