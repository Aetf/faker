
#! /usr/bin/env python

def case(str_arg):
    world(str_arg)
    print('call_group')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('see_part_for_other_world')
