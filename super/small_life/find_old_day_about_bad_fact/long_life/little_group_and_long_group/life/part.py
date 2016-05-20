
#! /usr/bin/env python

def person_or_fact(str_arg):
    point(str_arg)
    print('come_next_point')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person_or_fact('life_or_same_person')
