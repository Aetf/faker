
#! /usr/bin/env python

def new_woman(str_arg):
    problem(str_arg)
    print('call_child')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_woman('woman')
