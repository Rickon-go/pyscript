#!/usr/bin/env python

import subprocess

def uname_func():
    cmd='uname'
    arg='-a'
    print "sysinfo:"
    subprocess.call([cmd,arg])

def disk_func():
    cmd='df'
    arg='-h'
    print "sysinfo:"
    subprocess.call([cmd,arg])

def main():
    disk_func()
    uname_func()

if __name__=='__main__':
    main()
