
#! /usr/bin/env python

def see_thing(str_arg):
    bad_way_and_group(str_arg)
    print('long_life')

def bad_way_and_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_thing('know_different_eye_about_new_life')
