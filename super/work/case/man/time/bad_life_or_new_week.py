
#! /usr/bin/env python

def work(str_arg):
    own_child(str_arg)
    print('company')

def own_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('group_and_new_man')
