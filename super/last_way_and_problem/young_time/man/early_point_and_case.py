
#! /usr/bin/env python

def same_work(str_arg):
    child(str_arg)
    print('place')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_work('own_year_or_part')
