
#! /usr/bin/env python

def child(str_arg):
    bad_work_or_work(str_arg)
    print('thing')

def bad_work_or_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('good_life_and_first_number')
