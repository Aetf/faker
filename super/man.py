
#! /usr/bin/env python

def use_world(str_arg):
    man_or_number(str_arg)
    print('thing')

def man_or_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_world('use_large_company_for_few_point')
