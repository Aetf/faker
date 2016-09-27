
#! /usr/bin/env python

def good_case(str_arg):
    know_part(str_arg)
    print('same_life')

def know_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_case('tell_world')
