
#! /usr/bin/env python

def different_thing(str_arg):
    tell_time(str_arg)
    print('thing')

def tell_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_thing('ask_person')
