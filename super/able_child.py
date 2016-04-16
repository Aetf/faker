
#! /usr/bin/env python

def good_child(str_arg):
    life(str_arg)
    print('right_time')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_child('good_fact')
