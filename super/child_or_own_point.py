
#! /usr/bin/env python

def be_other_way(str_arg):
    get_work(str_arg)
    print('child')

def get_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    be_other_way('large_year')
