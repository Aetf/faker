
#! /usr/bin/env python

def think_new_place(str_arg):
    thing(str_arg)
    print('old_thing')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_new_place('time_or_world')
