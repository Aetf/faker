
#! /usr/bin/env python

def long_work(str_arg):
    long_thing(str_arg)
    print('old_part')

def long_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work('week')
