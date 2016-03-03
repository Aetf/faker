
#! /usr/bin/env python

def think_eye(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_eye('leave_important_government')
