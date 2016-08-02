
#! /usr/bin/env python

def public_case(str_arg):
    public_point(str_arg)
    print('go_point_into_point')

def public_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_case('new_week_or_government')
