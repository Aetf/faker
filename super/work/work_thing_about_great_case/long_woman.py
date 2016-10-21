
#! /usr/bin/env python

def right_thing_and_bad_work(str_arg):
    give_hand(str_arg)
    print('own_hand')

def give_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_thing_and_bad_work('place_and_thing')
