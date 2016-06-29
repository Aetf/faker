
#! /usr/bin/env python

def public_person(str_arg):
    look_public_fact(str_arg)
    print('know_child_about_fact')

def look_public_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_person('ask_part')
