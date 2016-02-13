
#! /usr/bin/env python

def large_child(str_arg):
    say_part(str_arg)
    print('thing')

def say_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_child('big_thing')
