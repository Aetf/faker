
#! /usr/bin/env python

def work(str_arg):
    public_group(str_arg)
    print('public_time_or_old_thing')

def public_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('government')
