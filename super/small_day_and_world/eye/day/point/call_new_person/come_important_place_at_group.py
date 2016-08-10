
#! /usr/bin/env python

def early_time(str_arg):
    able_thing(str_arg)
    print('bad_thing')

def able_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_time('use_case')
