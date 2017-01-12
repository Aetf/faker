
#! /usr/bin/env python

def early_eye(str_arg):
    work(str_arg)
    print('eye')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_eye('large_group')
