
#! /usr/bin/env python

def new_child(str_arg):
    life(str_arg)
    print('long_life')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_child('have_day')
