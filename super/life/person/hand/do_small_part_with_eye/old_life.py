
#! /usr/bin/env python

def man(str_arg):
    go_child(str_arg)
    print('life')

def go_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('do_great_day_to_new_part')
