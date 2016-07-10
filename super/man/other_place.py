
#! /usr/bin/env python

def time(str_arg):
    call_big_thing(str_arg)
    print('long_group')

def call_big_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('public_man_or_able_hand')
