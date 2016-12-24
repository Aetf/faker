
#! /usr/bin/env python

def time_and_child(str_arg):
    other_thing(str_arg)
    print('large_child_and_great_group')

def other_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_and_child('little_day')
