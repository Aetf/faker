
#! /usr/bin/env python

def man_and_thing(str_arg):
    new_place_or_fact(str_arg)
    print('important_time')

def new_place_or_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_and_thing('person')
