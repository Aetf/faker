
#! /usr/bin/env python

def public_thing(str_arg):
    woman(str_arg)
    print('want_woman')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('problem')
