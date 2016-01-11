
#! /usr/bin/env python

def other_thing(str_arg):
    important_fact(str_arg)
    print('important_hand')

def important_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_thing('thing')
