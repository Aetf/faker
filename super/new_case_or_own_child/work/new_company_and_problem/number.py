
#! /usr/bin/env python

def call_world_with_place(str_arg):
    hand(str_arg)
    print('day_and_next_hand')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_world_with_place('able_thing')
