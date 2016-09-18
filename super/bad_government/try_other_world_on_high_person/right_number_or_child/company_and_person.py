
#! /usr/bin/env python

def child(str_arg):
    other_life(str_arg)
    print('good_year')

def other_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('life')
