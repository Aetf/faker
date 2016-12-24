
#! /usr/bin/env python

def little_group(str_arg):
    part(str_arg)
    print('new_child')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_group('year_or_young_fact')
