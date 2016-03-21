
#! /usr/bin/env python

def go_thing(str_arg):
    woman(str_arg)
    print('time')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_thing('person')
