
#! /usr/bin/env python

def last_thing(str_arg):
    go_fact(str_arg)
    print('world')

def go_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    last_thing('week_and_hand')
