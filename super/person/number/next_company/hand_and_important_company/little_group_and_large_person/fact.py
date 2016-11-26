
#! /usr/bin/env python

def man(str_arg):
    public_work_or_number(str_arg)
    print('public_point')

def public_work_or_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('year')
