
#! /usr/bin/env python

def different_child(str_arg):
    man(str_arg)
    print('time')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_child('person')
