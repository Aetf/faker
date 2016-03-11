
#! /usr/bin/env python

def world(str_arg):
    work(str_arg)
    print('other_year')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('same_work_or_bad_life')
