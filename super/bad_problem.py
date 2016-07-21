
#! /usr/bin/env python

def other_woman(str_arg):
    bad_group(str_arg)
    print('other_thing')

def bad_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_woman('ask_part')
