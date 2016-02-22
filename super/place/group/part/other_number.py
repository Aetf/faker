
#! /usr/bin/env python

def small_work(str_arg):
    call_public_group_with_child(str_arg)
    print('company')

def call_public_group_with_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_work('company_and_high_hand')
