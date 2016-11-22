
#! /usr/bin/env python

def different_world(str_arg):
    government(str_arg)
    print('small_part')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_world('thing_and_hand')
