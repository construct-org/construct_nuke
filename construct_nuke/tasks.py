# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = [
    'setup_construct_nuke',
]

import os
from distutils.sysconfig import get_python_lib
from construct.tasks import (
    task,
    requires,
    success,
    params,
    store
)


@task
@requires(success('build_app_env'))
@params(store('app'))
def setup_construct_nuke(app):

    nuke_path = os.path.join(os.path.dirname(__file__), '.nuke')
    old_pypath = app.env.get('PYTHONPATH', '')
    pypath = os.pathsep.join([
        nuke_path,
        get_python_lib()
    ])
    if old_pypath:
        pypath += os.pathsep + old_pypath
    app.env['NUKE_PATH'] = nuke_path
    app.env['PYTHONPATH'] = pypath
