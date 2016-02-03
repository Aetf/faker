
#! /usr/bin/env python

def thing_or_eye(str_arg):
    thing(str_arg)
    print('important_company')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_or_eye('little_problem')
