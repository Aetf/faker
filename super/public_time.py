
#! /usr/bin/env python

def person(str_arg):
    own_person(str_arg)
    print('long_thing')

def own_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('eye')
