# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from os.path import isfile, join
import sys


def has_untitled_autosave():
    '''Returns True when there is an untitled autosave.

    If True, at startup, Nuke will launch the open autosave dialog.
    '''

    untitled_autosave = join(os.environ['NUKE_TEMP_DIR'], '.autosave')
    return isfile(untitled_autosave)


def has_autosave(nukescript):
    '''Returns True if the nukescript has an autosave file.autosave

    If True, Nuke will launch the open autosave dialog.
    '''

    return isfile(nukescript + '.autosave')


def show_file_open_at_startup():
    '''Returns True when there will be no autosave dialog at startup.'''

    # Check if Nuke was launched with a nuke script as an argument
    nuke_script = False
    for arg in sys.argv:
        if arg.endswith('.nk'):
            nuke_script = True

    if nuke_script or has_untitled_autosave():
        return False

    return True
