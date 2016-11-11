
#! /usr/bin/env python

def point(str_arg):
    thing(str_arg)
    print('work_or_thing')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('work_and_own_world')
