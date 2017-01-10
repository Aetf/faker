
#! /usr/bin/env python

def public_thing(str_arg):
    know_large_fact(str_arg)
    print('other_life')

def know_large_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('bad_way')
