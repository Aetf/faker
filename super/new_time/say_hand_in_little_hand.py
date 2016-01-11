
#! /usr/bin/env python

def look_man(str_arg):
    point(str_arg)
    print('child')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    look_man('work')
