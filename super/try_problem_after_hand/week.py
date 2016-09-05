
#! /usr/bin/env python

def point(str_arg):
    eye_or_right_world(str_arg)
    print('own_work')

def eye_or_right_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('child')
