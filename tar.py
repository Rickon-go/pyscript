#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
import shutil

name=sys.argv[1]
path=sys.argv[2]

def tar():
    shutil.make_archive(name,'gztar',path)

def main():
    tar()

if __name__=="__main__":
    main()
