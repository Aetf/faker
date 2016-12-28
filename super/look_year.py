
#! /usr/bin/env python

def call_large_work(str_arg):
    public_fact(str_arg)
    print('work_other_person')

def public_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_large_work('government')
