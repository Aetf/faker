
#! /usr/bin/env python

def world(str_arg):
    give_fact_about_life(str_arg)
    print('world')

def give_fact_about_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('high_year')
