
#! /usr/bin/env python

def place(str_arg):
    child(str_arg)
    print('good_company')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place('world')
