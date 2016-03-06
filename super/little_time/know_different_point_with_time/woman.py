
#! /usr/bin/env python

def thing(str_arg):
    child(str_arg)
    print('use_long_hand_over_way')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('next_point')
