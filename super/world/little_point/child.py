
#! /usr/bin/env python

def big_work(str_arg):
    child(str_arg)
    print('eye')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('first_part')
