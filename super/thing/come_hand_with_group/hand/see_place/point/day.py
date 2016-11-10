
#! /usr/bin/env python

def bad_fact(str_arg):
    time(str_arg)
    print('child')

def time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_fact('important_way_and_long_work')
