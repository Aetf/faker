
#! /usr/bin/env python

def case(str_arg):
    make_child(str_arg)
    print('thing')

def make_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('case_or_little_government')
