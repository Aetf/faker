
#! /usr/bin/env python

def public_world(str_arg):
    leave_day(str_arg)
    print('world')

def leave_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_world('child')
