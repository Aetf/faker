
#! /usr/bin/env python

def work(str_arg):
    large_part_and_work(str_arg)
    print('eye')

def large_part_and_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('important_number_and_company')
