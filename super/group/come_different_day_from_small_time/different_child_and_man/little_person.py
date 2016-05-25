
#! /usr/bin/env python

def long_number_or_child(str_arg):
    company(str_arg)
    print('child')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_number_or_child('have_old_work_beneath_child')
