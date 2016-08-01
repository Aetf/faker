
#! /usr/bin/env python

def government_and_bad_part(str_arg):
    government(str_arg)
    print('part')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    government_and_bad_part('last_man_or_next_company')
