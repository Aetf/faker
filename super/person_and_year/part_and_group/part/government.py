
#! /usr/bin/env python

def work_or_other_man(str_arg):
    long_person(str_arg)
    print('right_man')

def long_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_other_man('early_government')
