
#! /usr/bin/env python

def way(str_arg):
    eye(str_arg)
    print('child')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    way('feel_same_week')
