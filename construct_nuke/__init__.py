# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

__title__ = 'construct_nuke'
__description__ = 'Construct Nuke Integration'
__version__ = '0.0.1'
__author__ = 'Dan Bradham'
__email__ = 'danielbradham@gmail.com'
__license__ = 'MIT'
__url__ = 'https://github.com/construct-org/construct_nuke'

from construct_nuke import launcher
from construct_nuke.api import *


def available(ctx):
    return True


def register(cons):
    '''Register construct_nuke'''

    # Register launcher tasks
    launcher.register(cons)

    ctx = cons.get_context()
    if ctx.host == 'nuke':
        # Tasks available only from within nuke
        pass


def unregister(cons):
    '''Unregister construct_nuke'''

    # Unregister launcher tasks
    launcher.unregister(cons)

    ctx = cons.get_context()
    if ctx.host == 'nuke':
        # Tasks available only from within nuke
        pass
