
#! /usr/bin/env python

def child(str_arg):
    number(str_arg)
    print('last_group')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('new_part')
