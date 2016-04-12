
#! /usr/bin/env python

def high_world(str_arg):
    thing(str_arg)
    print('good_child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    high_world('bad_time')
