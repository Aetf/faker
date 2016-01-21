
#! /usr/bin/env python

def public_thing(str_arg):
    number(str_arg)
    print('know_old_child')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('first_number')
