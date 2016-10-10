
#! /usr/bin/env python

def public_case(str_arg):
    case(str_arg)
    print('number')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_case('company')
