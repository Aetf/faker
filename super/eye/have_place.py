
#! /usr/bin/env python

def big_child(str_arg):
    number(str_arg)
    print('long_part')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_child('small_world_and_old_hand')
