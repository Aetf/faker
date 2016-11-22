
#! /usr/bin/env python

def child(str_arg):
    own_man(str_arg)
    print('first_year')

def own_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('thing')
