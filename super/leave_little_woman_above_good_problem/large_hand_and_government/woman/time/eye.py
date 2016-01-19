
#! /usr/bin/env python

def work(str_arg):
    use_eye(str_arg)
    print('see_child')

def use_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('take_work')
