
#! /usr/bin/env python

def try_small_work(str_arg):
    early_person(str_arg)
    print('different_way')

def early_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_small_work('person')
