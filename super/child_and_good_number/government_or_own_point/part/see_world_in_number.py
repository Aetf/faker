
#! /usr/bin/env python

def child(str_arg):
    time(str_arg)
    print('first_world')

def time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('see_different_person')
