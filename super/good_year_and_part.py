
#! /usr/bin/env python

def be_fact(str_arg):
    come_early_thing(str_arg)
    print('old_world')

def come_early_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    be_fact('case')
