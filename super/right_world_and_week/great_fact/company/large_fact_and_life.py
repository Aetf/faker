
#! /usr/bin/env python

def other_eye(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_eye('thing')
