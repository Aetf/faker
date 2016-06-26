
#! /usr/bin/env python

def bad_child(str_arg):
    child(str_arg)
    print('small_way')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_child('good_company')
