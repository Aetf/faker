
#! /usr/bin/env python

def thing(str_arg):
    different_thing(str_arg)
    print('world')

def different_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('feel_part')
