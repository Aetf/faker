
#! /usr/bin/env python

def work(str_arg):
    tell_case(str_arg)
    print('leave_other_person')

def tell_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('case')
