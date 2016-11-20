
#! /usr/bin/env python

def thing(str_arg):
    big_part(str_arg)
    print('life')

def big_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('person')
