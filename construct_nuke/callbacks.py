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
    set_context_to_nuke_script()


def on_script_load():
    '''onScriptLoad callback'''

    import nuke
    _log.debug('on_script_load')
    set_context_to_nuke_script()


def set_context_to_nuke_script():
    '''Sets the Context to the current nuke script, if it is in a workspace'''

    import nuke

    host = construct.get_host()
    path = host.get_filepath()

    new_ctx = construct.Context.from_path(path)
    new_ctx.file = path

    if new_ctx.workspace:
        _log.debug('Setting context to %s' % path)
        construct.set_context(new_ctx)
        host.set_workspace(new_ctx.workspace.path)
        new_ctx.to_env()
    else:
        _log.debug(
            'Not setting context. '
            'Script is not in a construct workspace...'
        )



def register():
    '''Register construct_nuke callbacks'''

    import nuke
    nuke.addOnScriptLoad(on_script_load)
    nuke.addOnScriptSave(on_script_save)
