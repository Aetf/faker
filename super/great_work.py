
#! /usr/bin/env python

def work_and_child(str_arg):
    old_world(str_arg)
    print('seem_point')

def old_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_and_child('bad_person_or_company')
