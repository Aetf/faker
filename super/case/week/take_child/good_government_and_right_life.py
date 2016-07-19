
#! /usr/bin/env python

def think_child(str_arg):
    time_or_same_life(str_arg)
    print('different_day')

def time_or_same_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_child('want_child')
