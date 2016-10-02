
#! /usr/bin/env python

def man(str_arg):
    hand(str_arg)
    print('child')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('point')
