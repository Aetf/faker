
#! /usr/bin/env python

def number_or_work(str_arg):
    big_child(str_arg)
    print('first_place')

def big_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number_or_work('other_world')
