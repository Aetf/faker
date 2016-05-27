
#! /usr/bin/env python

def early_number_or_child(str_arg):
    child(str_arg)
    print('large_work')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_number_or_child('day')
