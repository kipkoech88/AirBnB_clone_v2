#!/usr/bin/env python3
"""
package static file
as archives to be deployed
on nginx
"""
import os
from fabric import *
from datetime import datetime


def do_pack():
    """ check if the versions
    folder exists and if not
    create a new one """
    if not os.path.exists("versions"):
        local("mkdir versions")
    now = datetime.now
    archfile = "versions/web_static_{}.tgz".format(
                now.strftime("%Y%m%D%H%M%S"))
    command = "tar -cfv {} {}".format(archfile, "web_static")
    res = local(command)
    if not res.failed:
        return archfile
