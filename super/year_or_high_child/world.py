
#! /usr/bin/env python

def good_way(str_arg):
    group(str_arg)
    print('group_or_same_problem')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_way('big_work')
