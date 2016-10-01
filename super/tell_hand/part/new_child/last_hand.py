
#! /usr/bin/env python

def thing(str_arg):
    world(str_arg)
    print('life')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('week_or_way')
