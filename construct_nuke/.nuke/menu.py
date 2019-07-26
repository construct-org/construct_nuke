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
callbacks.set_favorite_dirs()

_log.debug('Creating Construct menu...')
menus.setup_construct_menu()

if utils.show_file_open_at_startup():
    # TODO: Add abstraction around creating ActionForms
    # This entire block can be reduced to an api call as nothing is specific
    # to nuke. Maybe...construct.interact('file.open')?
    host = construct.get_host()
    ctx = construct.get_context()

    if ctx.workspace and not host.get_filename():
        if ctx.workspace.get_work_files():
            action_identifier = 'file.open'
        else:
            action_identifier = 'file.save'

        construct.show_form(action_identifier)
