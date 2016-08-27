
#! /usr/bin/env python

def bad_child(str_arg):
    thing(str_arg)
    print('point')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_child('eye')
