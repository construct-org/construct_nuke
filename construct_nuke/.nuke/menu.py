# -*- coding: utf-8 -*-
from __future__ import absolute_import
import construct_nuke.callbacks
import logging

_log = logging.getLogger('construct.nuke.menu')
_log.debug('Registering callbacks')
construct_nuke.callbacks.register()
construct_nuke.callbacks.set_favorite_dirs()
