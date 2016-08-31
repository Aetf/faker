
#! /usr/bin/env python

def same_work(str_arg):
    early_child(str_arg)
    print('big_case_and_right_fact')

def early_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_work('own_child')
