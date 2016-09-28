
#! /usr/bin/env python

def come_case_under_child(str_arg):
    woman(str_arg)
    print('child')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    come_case_under_child('first_point')
