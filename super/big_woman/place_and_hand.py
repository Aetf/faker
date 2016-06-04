
#! /usr/bin/env python

def work(str_arg):
    big_child(str_arg)
    print('young_group')

def big_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('place_or_bad_time')
