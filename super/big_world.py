
#! /usr/bin/env python

def child(str_arg):
    get_eye(str_arg)
    print('point')

def get_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('give_thing')
