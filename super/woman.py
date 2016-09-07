
#! /usr/bin/env python

def use_case_under_group(str_arg):
    work_public_day(str_arg)
    print('different_year_or_group')

def work_public_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_case_under_group('public_fact')
