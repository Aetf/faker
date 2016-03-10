
#! /usr/bin/env python

def thing(str_arg):
    person(str_arg)
    print('great_man')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('old_thing')
