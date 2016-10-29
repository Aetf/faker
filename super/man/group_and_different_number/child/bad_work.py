
#! /usr/bin/env python

def company_and_small_fact(str_arg):
    public_man(str_arg)
    print('other_man')

def public_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company_and_small_fact('early_woman')
