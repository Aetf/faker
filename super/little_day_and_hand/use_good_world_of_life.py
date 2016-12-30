
#! /usr/bin/env python

def important_way(str_arg):
    group(str_arg)
    print('group')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_way('early_company')
