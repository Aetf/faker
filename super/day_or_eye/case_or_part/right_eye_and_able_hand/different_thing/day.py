
#! /usr/bin/env python

def try_time(str_arg):
    big_child(str_arg)
    print('next_number_and_work')

def big_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_time('man')
