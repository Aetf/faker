
#! /usr/bin/env python

def child(str_arg):
    thing(str_arg)
    print('day')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('old_year')
