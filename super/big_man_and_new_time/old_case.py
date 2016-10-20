
#! /usr/bin/env python

def child(str_arg):
    next_thing(str_arg)
    print('person')

def next_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('get_group')
