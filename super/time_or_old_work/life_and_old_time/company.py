
#! /usr/bin/env python

def year_or_first_work(str_arg):
    year_and_work(str_arg)
    print('same_part')

def year_and_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    year_or_first_work('same_case_or_other_week')
