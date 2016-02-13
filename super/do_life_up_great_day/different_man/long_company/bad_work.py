
#! /usr/bin/env python

def public_thing(str_arg):
    work(str_arg)
    print('day')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('week_or_new_man')
