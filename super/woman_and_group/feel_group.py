
#! /usr/bin/env python

def little_part(str_arg):
    tell_child(str_arg)
    print('part')

def tell_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_part('good_company')
