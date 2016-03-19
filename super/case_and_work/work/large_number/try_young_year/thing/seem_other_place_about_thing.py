
#! /usr/bin/env python

def seem_work(str_arg):
    ask_group_to_first_child(str_arg)
    print('other_thing')

def ask_group_to_first_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    seem_work('want_fact')
