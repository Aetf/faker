
#! /usr/bin/env python

def child(str_arg):
    large_child(str_arg)
    print('person')

def large_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('go_point')
