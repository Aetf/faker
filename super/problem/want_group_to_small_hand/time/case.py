
#! /usr/bin/env python

def child(str_arg):
    day(str_arg)
    print('own_life')

def day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('know_large_life')
