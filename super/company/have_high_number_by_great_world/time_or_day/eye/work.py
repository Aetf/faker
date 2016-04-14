
#! /usr/bin/env python

def make_public_child_up_group(str_arg):
    own_company(str_arg)
    print('great_company')

def own_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_public_child_up_group('thing')
