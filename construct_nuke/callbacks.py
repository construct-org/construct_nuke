# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging
import os
import construct

_log = logging.getLogger('construct.nuke.callbacks')


def on_script_save():
    '''onScriptSave callback'''

    import nuke
    _log.debug('on_script_save')
    # TODO: Check save path
    set_context_to_nuke_script()
    set_favorite_dirs()


def on_script_load():
    '''onScriptLoad callback'''

    import nuke
    _log.debug('on_script_load')
    set_context_to_nuke_script()
    set_favorite_dirs()


def set_context_to_nuke_script():
    '''Sets the Context to the current nuke script, if it is in a workspace'''

    import nuke

    root = nuke.root()
    name = root['name'].value()
    path = os.path.dirname(name)

    new_ctx = construct.Context.from_path(path)
    if new_ctx.workspace:
        _log.debug('Setting context to %s' % path)
        construct.set_context(new_ctx)
    else:
        _log.debug(
            'Not setting context. '
            'Script is not in a construct workspace...'
        )


def set_favorite_dirs():
    '''Sets up favorite directories for current context'''
    import nuke

    _log.debug('setting favorite dirs')

    ctx = construct.get_context()
    if ctx.workspace:
        nuke.addFavoriteDir(
            'Workspace',
            ctx.workspace.path,
            nuke.IMAGE | nuke.SCRIPT,
            'Current construct workspace'
        )

    # TODO: Add renders directory


def register():
    '''Register construct_nuke callbacks'''

    import nuke
    nuke.addOnScriptLoad(on_script_load)
    nuke.addOnScriptSave(on_script_save)
