
#! /usr/bin/env python

def go_group(str_arg):
    fact(str_arg)
    print('world')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_group('long_hand_and_man')
