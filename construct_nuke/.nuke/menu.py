# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging

import construct
from construct_ui import resources
from construct_nuke import callbacks, utils, menus


_log = logging.getLogger('construct.nuke.menu')
resources.init()

_log.debug('Registering callbacks')
callbacks.register()

_log.debug('Creating Construct menu...')
menus.setup_construct_menu()

ctx = construct.get_context()

if ctx.workspace:
    host = construct.get_host()
    host.set_workspace(ctx.workspace.path)

if utils.show_dialog_at_startup():
    if ctx.workspace and not host.get_filename():
        if ctx.workspace.get_work_files():
            action_identifier = 'file.open'
        else:
            action_identifier = 'file.save'

        construct.show_form(action_identifier)
