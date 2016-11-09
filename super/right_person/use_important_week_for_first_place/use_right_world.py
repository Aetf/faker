
#! /usr/bin/env python

def child(str_arg):
    problem_and_place(str_arg)
    print('point')

def problem_and_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('thing')
