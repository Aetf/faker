
#! /usr/bin/env python

def child(str_arg):
    last_life(str_arg)
    print('make_other_part')

def last_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('last_eye')
