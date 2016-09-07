
#! /usr/bin/env python

def child(str_arg):
    seem_part(str_arg)
    print('same_group')

def seem_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('bad_way_or_small_world')
