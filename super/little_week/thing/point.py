
#! /usr/bin/env python

def work(str_arg):
    same_place(str_arg)
    print('feel_case_after_work')

def same_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('long_year')
