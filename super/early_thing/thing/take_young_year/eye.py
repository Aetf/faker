
#! /usr/bin/env python

def world(str_arg):
    next_part(str_arg)
    print('call_thing_under_last_hand')

def next_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('number')
