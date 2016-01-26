
#! /usr/bin/env python

def call_small_man_about_part(str_arg):
    woman(str_arg)
    print('own_place_and_own_case')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_small_man_about_part('use_last_eye')
