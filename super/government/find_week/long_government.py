
#! /usr/bin/env python

def own_thing(str_arg):
    problem(str_arg)
    print('child')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_thing('hand')
