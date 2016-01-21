
#! /usr/bin/env python

def eye_and_man(str_arg):
    child(str_arg)
    print('number')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_and_man('world')
