
#! /usr/bin/env python

def part_or_case(str_arg):
    old_part(str_arg)
    print('own_case')

def old_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part_or_case('call_place_after_place')
