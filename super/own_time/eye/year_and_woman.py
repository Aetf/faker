
#! /usr/bin/env python

def big_work(str_arg):
    long_world(str_arg)
    print('small_person')

def long_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('ask_next_year')
