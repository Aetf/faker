
#! /usr/bin/env python

def own_work(str_arg):
    go_other_place(str_arg)
    print('high_world')

def go_other_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_work('case')
