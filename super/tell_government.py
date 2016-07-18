
#! /usr/bin/env python

def thing(str_arg):
    bad_group(str_arg)
    print('next_hand')

def bad_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('right_way')
