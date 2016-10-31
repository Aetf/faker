
#! /usr/bin/env python

def good_child(str_arg):
    ask_great_place(str_arg)
    print('work')

def ask_great_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_child('find_great_part')
