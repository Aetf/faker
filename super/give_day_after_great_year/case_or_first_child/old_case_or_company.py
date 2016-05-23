
#! /usr/bin/env python

def thing(str_arg):
    small_child(str_arg)
    print('feel_last_time')

def small_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('group')
