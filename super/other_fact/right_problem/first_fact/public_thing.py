
#! /usr/bin/env python

def thing(str_arg):
    hand(str_arg)
    print('man')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('big_number')
