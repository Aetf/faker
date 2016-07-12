
#! /usr/bin/env python

def large_company_and_own_company(str_arg):
    public_child(str_arg)
    print('work_or_child')

def public_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_company_and_own_company('important_part')
