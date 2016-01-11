
#! /usr/bin/env python

def make_own_company_on_other_man(str_arg):
    public_company_and_thing(str_arg)
    print('child')

def public_company_and_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_own_company_on_other_man('government')
