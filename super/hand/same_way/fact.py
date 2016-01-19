
#! /usr/bin/env python

def man(str_arg):
    try_company_after_case(str_arg)
    print('last_company')

def try_company_after_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('different_government')
