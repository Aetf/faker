
#! /usr/bin/env python

def thing(str_arg):
    person(str_arg)
    print('have_world')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('day')
