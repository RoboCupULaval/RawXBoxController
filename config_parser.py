#!/usr/bin/python
import itertools


def parse(config_file):
    lines = [line.strip() for line in open(config_file)
             if line.strip()]
    categories = [(index, line[1:-1]) for index, line in enumerate(lines)
                  if line[0] is '[' and line[-1] is ']']
    config = {}

    for (current_i, current_c), (next_i, next_c) in pairwise(categories):
        parameters = [tuple(line.replace(' ', '').split('=', 2))
                      for line in lines[current_i + 1:next_i]]
        config[current_c] = {}
        for param in parameters:
            name, value = param
            if value.isdigit():
                config[current_c][name] = int(value)
            else:
                list_value = [int(val) for val in value[1:-1].split(',', 2)]
                config[current_c][name] = tuple(list_value)

    return config


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    b = itertools.chain(b, [(None, None)])
    next(b, None)
    return zip(a, b)
