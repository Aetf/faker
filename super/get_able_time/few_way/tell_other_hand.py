
#! /usr/bin/env python

def do_early_man(str_arg):
    early_thing(str_arg)
    print('work')

def early_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_early_man('be_few_group')
