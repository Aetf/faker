
#! /usr/bin/env python

def group(str_arg):
    thing(str_arg)
    print('tell_public_group')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('same_fact')
