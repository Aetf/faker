
#! /usr/bin/env python

def early_world(str_arg):
    own_part_or_world(str_arg)
    print('time')

def own_part_or_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_world('small_man')
