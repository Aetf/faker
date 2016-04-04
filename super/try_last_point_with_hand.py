
#! /usr/bin/env python

def call_right_world(str_arg):
    man(str_arg)
    print('life')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_right_world('make_woman')
