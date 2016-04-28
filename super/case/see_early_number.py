
#! /usr/bin/env python

def take_little_work_on_public_year(str_arg):
    work(str_arg)
    print('different_year')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_little_work_on_public_year('little_week')
