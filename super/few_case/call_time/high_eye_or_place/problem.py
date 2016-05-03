
#! /usr/bin/env python

def try_child(str_arg):
    new_life(str_arg)
    print('thing')

def new_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_child('call_early_part_at_bad_eye')
