
#! /usr/bin/env python

def thing(str_arg):
    part(str_arg)
    print('say_public_work')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('get_long_place')
