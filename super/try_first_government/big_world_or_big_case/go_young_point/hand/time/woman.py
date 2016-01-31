
#! /usr/bin/env python

def thing_and_bad_work(str_arg):
    work_next_group(str_arg)
    print('old_year')

def work_next_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_bad_work('own_case')
