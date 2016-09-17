
#! /usr/bin/env python

def different_thing(str_arg):
    different_work(str_arg)
    print('day')

def different_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_thing('hand')
