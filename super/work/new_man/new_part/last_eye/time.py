
#! /usr/bin/env python

def see_case(str_arg):
    work(str_arg)
    print('child_or_man')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_case('try_government')
