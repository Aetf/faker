
#! /usr/bin/env python

def child(str_arg):
    life(str_arg)
    print('life')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('part')
