
#! /usr/bin/env python

def company_or_government(str_arg):
    big_group_or_early_group(str_arg)
    print('government')

def big_group_or_early_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company_or_government('early_child_or_child')
