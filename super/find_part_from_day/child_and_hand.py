
#! /usr/bin/env python

def long_eye(str_arg):
    bad_child(str_arg)
    print('big_case')

def bad_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_eye('eye_or_part')
