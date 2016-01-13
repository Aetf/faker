
#! /usr/bin/env python

def eye_and_public_thing(str_arg):
    child(str_arg)
    print('thing')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_and_public_thing('early_place')
