# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import construct
from construct_ui import resources
from construct_ui.menus import ActionMenu
from construct_nuke import callbacks, utils

_log = logging.getLogger('construct.nuke.menu')
_log.debug('Registering callbacks')
callbacks.register()
callbacks.set_favorite_dirs()

_log.debug('Creating Construct menu...')
menubar = utils.get_nuke_menubar()
menubar.addMenu(ActionMenu('Construct', menubar))


if utils.show_file_open_at_startup():
    # TODO: Add abstraction around creating ActionForms
    # This entire block can be reduced to an api call as nothing is specific
    # to nuke. Maybe...construct.interact('file.open')?
    host = construct.get_host()
    ctx = construct.get_context()
    if ctx.workspace and not host.get_filename():
        action = construct.actions.get('file.open')
        parent = host.get_qt_parent()
        form_cls = construct.get_form(action.identifier)
        form = form_cls(action, ctx, parent)
        form.setStyleSheet(resources.style('dark'))
        form.show()
