
#! /usr/bin/env python

def old_thing(str_arg):
    other_work(str_arg)
    print('think_week')

def other_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_thing('work')
