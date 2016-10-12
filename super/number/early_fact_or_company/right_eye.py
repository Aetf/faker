
#! /usr/bin/env python

def public_thing(str_arg):
    bad_company_or_government(str_arg)
    print('think_hand')

def bad_company_or_government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('company')
