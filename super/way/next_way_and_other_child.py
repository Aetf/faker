
#! /usr/bin/env python

def child(str_arg):
    woman(str_arg)
    print('woman')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('good_child_or_place')
