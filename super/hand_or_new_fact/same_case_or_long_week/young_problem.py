
#! /usr/bin/env python

def big_work(str_arg):
    own_man(str_arg)
    print('work_public_man')

def own_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('high_work')
