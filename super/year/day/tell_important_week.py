
#! /usr/bin/env python

def child(str_arg):
    take_part(str_arg)
    print('number')

def take_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('problem')
