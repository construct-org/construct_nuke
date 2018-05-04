# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging
from construct_ui.menus import ActionMenu
from construct_nuke import callbacks
from construct_nuke.ui import get_nuke_menubar


_log = logging.getLogger('construct.nuke.menu')
_log.debug('Registering callbacks')
callbacks.register()
callbacks.set_favorite_dirs()


_log.debug('Creating Construct menu...')
menubar = get_nuke_menubar()
menubar.addMenu(ActionMenu('Construct', menubar))
