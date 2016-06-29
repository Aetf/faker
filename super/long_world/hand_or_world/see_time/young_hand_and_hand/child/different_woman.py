
#! /usr/bin/env python

def work(str_arg):
    see_bad_child(str_arg)
    print('group_or_work')

def see_bad_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('big_fact')
