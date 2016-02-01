
#! /usr/bin/env python

def little_problem(str_arg):
    try_point(str_arg)
    print('child_and_work')

def try_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_problem('seem_long_work')
