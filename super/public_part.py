
#! /usr/bin/env python

def small_life(str_arg):
    child(str_arg)
    print('new_time')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_life('way')
