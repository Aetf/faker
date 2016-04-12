
#! /usr/bin/env python

def tell_early_fact_with_bad_fact(str_arg):
    man(str_arg)
    print('other_way')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_early_fact_with_bad_fact('life_or_other_week')
