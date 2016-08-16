
#! /usr/bin/env python

def try_thing(str_arg):
    person(str_arg)
    print('number')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_thing('thing_or_life')
