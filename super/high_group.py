
#! /usr/bin/env python

def long_child(str_arg):
    problem_and_eye(str_arg)
    print('tell_bad_point')

def problem_and_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_child('thing')
