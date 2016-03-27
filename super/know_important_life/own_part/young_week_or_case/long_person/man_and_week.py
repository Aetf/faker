
#! /usr/bin/env python

def public_work(str_arg):
    government(str_arg)
    print('part')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_work('problem')
