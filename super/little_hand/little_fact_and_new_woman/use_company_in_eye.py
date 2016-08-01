
#! /usr/bin/env python

def life(str_arg):
    child(str_arg)
    print('say_long_part')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('try_great_part')
