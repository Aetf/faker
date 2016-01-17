
#! /usr/bin/env python

def see_thing_beneath_good_work(str_arg):
    work(str_arg)
    print('other_problem')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_thing_beneath_good_work('other_day')
