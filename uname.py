#!/usr/bin/env python
import subprocess

#command
uname='uname'
uname_arg='-a'
print "Gathering system information with %s command:" % uname
subprocess.call([uname,uname_arg])

