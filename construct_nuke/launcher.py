# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

__all__ = [
    'setup_construct_nuke',
    'register',
    'unregister',
]

import os
import subprocess
from construct_launcher import BEFORE_LAUNCH
from construct import (
    task,
    requires,
    success,
    params,
    store,
    returns
)


@task(priority=BEFORE_LAUNCH)
@requires(success('build_app_env'))
@params(store('app'))
@returns(store('app'))
def setup_construct_nuke(app):

    nuke_path = os.path.join(os.path.dirname(__file__), '.nuke')
    pypath = os.pathsep.join([
        userSetup,
        app['env'].get('PYTHONPATH', ''),
        os.path.join(os.path.dirname(__file__), '..')
    ])
    app['env']['NUKE_PATH'] = scpath
    app['env']['PYTHONPATH'] = pypath
    return app


def register(cons):

    cons.action_hub.connect('launch.nuke*', setup_construct_nuke)


def unregister(cons):

    cons.action_hub.disconnect('launch.nuke*', setup_construct_nuke)
