
#! /usr/bin/env python

def early_fact(str_arg):
    public_fact(str_arg)
    print('long_time')

def public_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_fact('be_own_place_under_number')
