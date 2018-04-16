# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging
import construct
import nuke


_log = logging.getLogger('construct.nuke.init')
construct.init()

ctx = construct.get_context()
_log.debug('Setting workspace: %s' % ctx.workspace.path)
if ctx.workspace:
    os.chdir(ctx.workspace.path)

nuke.knobDefault("Root.project_directory", ctx.workspace.path)
nuke.knobDefault("Root.format", "HD_1080")
