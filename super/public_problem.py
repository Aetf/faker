
#! /usr/bin/env python

def bad_child(str_arg):
    high_place(str_arg)
    print('tell_big_woman_in_place')

def high_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_child('same_case_or_fact')
