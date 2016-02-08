
#! /usr/bin/env python

def man_or_other_man(str_arg):
    early_point(str_arg)
    print('great_time')

def early_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_or_other_man('world')
