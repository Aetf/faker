
#! /usr/bin/env python

def public_fact(str_arg):
    thing_or_fact(str_arg)
    print('first_time')

def thing_or_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_fact('get_first_point_about_work')
