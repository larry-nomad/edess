#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
import signal
import time
from flaskext.actions import Manager
import settings
from sony_o2o import app
from flaskext.actions.fastcgi import runfastcgi
from o2olib.utils import utils
from o2olib import logger

app.config.from_object(settings)
manager = Manager(app, default_server_actions=True)


def _start_server_action():
    print "starting web..."
    kwargs = {
        "protocol": "fcgi",
        "host": settings.FCGI_HOST,
        "port": settings.FCGI_PORT,
        "method": "fork",
        "pidfile": settings.WEB_PID_FILE,
        "debug": False,
        "daemonize": True
    }
    runfastcgi(app, **kwargs)


@manager.register("start_server")
def start_server(app):
    return _start_server_action


def _stop_server_action():
    # Get the pid from the pidfile
    try:
        fp = open(settings.WEB_PID_FILE, 'r')
        pid = int(fp.read().strip())
        fp.close()
    except IOError:
        pid = None

    if not pid:
        message = "pidfile %s does not exist. " + \
                  "Daemon not running?\n"
        sys.stderr.write(message % settings.WEB_PID_FILE)
        return  # not an error in a restart

    sys.stdout.write("Service stopping ")
    sys.stdout.flush()
    # Try killing the daemon process
    try:
        while 1:
            os.kill(pid, signal.SIGTERM)
            time.sleep(1)
            sys.stdout.write(".")
            sys.stdout.flush()
    except OSError, err:
        e = str(err.args)
        if e.find("No such process") > 0:
            if os.path.exists(settings.WEB_PID_FILE):
                os.remove(settings.WEB_PID_FILE)
            else:
                print (str(err.args))
                sys.exit(1)

    sys.stdout.write("  [OK]\n")


@manager.register("stop_server")
def stop_server(app):
    return _stop_server_action


def _restart_server_action():
    _stop_server_action()
    _start_server_action()


@manager.register("restart_server")
def restart_server(app):
    return _restart_server_action


if __name__ == "__main__":
    # setup logger
    if not utils.setupLogger(settings.LOG_PATH, settings.LOG_WEB_NAME):
        print 'setup logger error.'
        sys.exit(2)

    logger.Logger().disableDebug()

    # manager run
    manager.run()
