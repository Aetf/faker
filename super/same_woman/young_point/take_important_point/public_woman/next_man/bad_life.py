
#! /usr/bin/env python

def go_other_child(str_arg):
    go_first_group(str_arg)
    print('tell_life_of_bad_fact')

def go_first_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_other_child('see_different_thing')
