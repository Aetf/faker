
#! /usr/bin/env python

def call_small_child_about_good_week(str_arg):
    child(str_arg)
    print('right_world')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_small_child_about_good_week('own_place_and_few_woman')
