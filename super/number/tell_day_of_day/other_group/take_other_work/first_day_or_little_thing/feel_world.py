
#! /usr/bin/env python

def work(str_arg):
    right_man(str_arg)
    print('early_man')

def right_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('year')
