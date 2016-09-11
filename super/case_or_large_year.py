
#! /usr/bin/env python

def eye(str_arg):
    call_bad_part(str_arg)
    print('say_first_place')

def call_bad_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('different_time')
