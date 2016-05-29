
#! /usr/bin/env python

def work_or_same_way(str_arg):
    make_little_number(str_arg)
    print('next_thing')

def make_little_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_same_way('large_work')
