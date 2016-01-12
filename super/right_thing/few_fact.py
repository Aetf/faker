
#! /usr/bin/env python

def different_thing(str_arg):
    person(str_arg)
    print('child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_thing('hand')
