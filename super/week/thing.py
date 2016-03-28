
#! /usr/bin/env python

def large_work(str_arg):
    child(str_arg)
    print('get_bad_company_from_right_way')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_work('big_man')
