
#! /usr/bin/env python

def thing(str_arg):
    person(str_arg)
    print('part')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('high_hand')
