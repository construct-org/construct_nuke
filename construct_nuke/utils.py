# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from os.path import isfile, join
import sys


def get_top_level_widget(widget_cls=None):
    '''Useful to obtain the top level Nuke QMainWindow.

    Every dialog needs to be parented to something in Nuke, otherwise they
    could be consumed python's garbage collector.
    '''

    from Qt import QtWidgets
    widget_cls = widget_cls or QtWidgets.QWidget
    for widget in QtWidgets.QApplication.instance().topLevelWidgets():
        if isinstance(widget, widget_cls):
            return widget


def get_nuke_menubar():
    '''Get Nuke's QMenuBar Widget.

    We can parent our own QMenu's to this guy, instead of using nukes built-in
    menu commands.
    '''

    from Qt import QtWidgets
    for widget in QtWidgets.QApplication.instance().allWidgets():
        if isinstance(widget, QtWidgets.QMenuBar):
            return widget


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

    # Get the nuke script that the Nuke command was passed
    nuke_script = False
    for arg in sys.argv:
        if arg.endswith('.nk'):
            nuke_script = True

    if nuke_script or has_untitled_autosave():
        return False

    return True
