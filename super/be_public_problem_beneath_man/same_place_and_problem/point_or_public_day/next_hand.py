
#! /usr/bin/env python

def thing(str_arg):
    take_world(str_arg)
    print('child')

def take_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('high_life_and_man')
