
#! /usr/bin/env python

def tell_man(str_arg):
    first_fact_or_case(str_arg)
    print('bad_thing')

def first_fact_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_man('early_hand')
