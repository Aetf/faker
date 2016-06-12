
#! /usr/bin/env python

def right_work(str_arg):
    have_important_fact_of_first_day(str_arg)
    print('other_case')

def have_important_fact_of_first_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_work('government_and_child')
