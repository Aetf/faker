
#! /usr/bin/env python

def leave_great_thing(str_arg):
    next_group(str_arg)
    print('last_group')

def next_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_great_thing('tell_same_year')
