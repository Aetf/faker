
#! /usr/bin/env python

def different_eye(str_arg):
    do_bad_case(str_arg)
    print('do_group')

def do_bad_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_eye('child')
