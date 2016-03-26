
#! /usr/bin/env python

def hand(str_arg):
    think_hand(str_arg)
    print('important_hand')

def think_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('thing')
