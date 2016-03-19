
#! /usr/bin/env python

def time_or_large_eye(str_arg):
    ask_group(str_arg)
    print('child')

def ask_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_or_large_eye('good_case')
