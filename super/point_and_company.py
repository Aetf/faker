
#! /usr/bin/env python

def other_child(str_arg):
    life(str_arg)
    print('early_man_and_year')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('time')
