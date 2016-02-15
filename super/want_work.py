
#! /usr/bin/env python

def case_or_government(str_arg):
    work(str_arg)
    print('other_government')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case_or_government('first_case')
