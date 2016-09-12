
#! /usr/bin/env python

def man_and_old_world(str_arg):
    thing(str_arg)
    print('child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_and_old_world('want_time')
