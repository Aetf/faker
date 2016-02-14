
#! /usr/bin/env python

def day(str_arg):
    call_world(str_arg)
    print('own_year')

def call_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    day('say_small_time')
