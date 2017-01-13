#! /usr/bin/env python
import os
from subprocess import check_call


def cmd_wrap(*args):
    return args


def str_wrap(s):
    return '"' + s + '"'


# git
def git_init():
    cmd = cmd_wrap('git', 'init')
    check_call(cmd)


def git_add(files):
    cmd = cmd_wrap('git', 'add', *files)
    check_call(cmd)


def git_tag(tag):
    cmd = cmd_wrap('git', 'tag', tag)
    check_call(cmd)


def git_commit(msg, date=None):
    cmds = ['git', 'commit', '-m', str_wrap(msg)]
    if date is not None:
        cmds = ['env',
                'GIT_AUTHOR_DATE={}'.format(date.isoformat()),
                'GIT_COMMITTER_DATE={}'.format(date.isoformat())] + cmds
    cmd = cmd_wrap(*cmds)
    check_call(cmd)


def git_rm(files):
    cmd = cmd_wrap('git', 'rm', '--ignore-unmatch', '-rf', *files)
    check_call(cmd)


def git(files, msg):
    git_add(files)
    git_commit(msg)


# date
def mod_date(dt):
    cmd = cmd_wrap('sudo', 'date', '-s', str_wrap(dt))
    check_call(cmd)


# mkdir
def mkdir(dir_name):
    if dir_name and (not os.path.exists(dir_name)):
        os.makedirs(dir_name)
