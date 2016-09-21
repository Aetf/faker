
#! /usr/bin/env python

def person(str_arg):
    next_thing_and_bad_person(str_arg)
    print('public_way')

def next_thing_and_bad_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('same_way')
