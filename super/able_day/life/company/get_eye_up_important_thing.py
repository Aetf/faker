
#! /usr/bin/env python

def other_woman(str_arg):
    man(str_arg)
    print('new_case')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_woman('feel_world')
