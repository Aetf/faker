
#! /usr/bin/env python

def child(str_arg):
    different_life(str_arg)
    print('own_eye')

def different_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('work')
