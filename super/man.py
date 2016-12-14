
#! /usr/bin/env python

def big_child(str_arg):
    child(str_arg)
    print('time')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_child('call_high_hand_over_hand')
