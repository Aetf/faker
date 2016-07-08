
#! /usr/bin/env python

def child(str_arg):
    eye(str_arg)
    print('group')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('other_week')
