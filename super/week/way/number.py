
#! /usr/bin/env python

def new_thing_and_early_group(str_arg):
    early_thing(str_arg)
    print('man')

def early_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_thing_and_early_group('try_thing')
