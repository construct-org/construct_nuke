# -*- coding: utf-8 -*-
from __future__ import absolute_import


def get_nuke_menubar():
    '''Get Nuke's QMenuBar Widget.

    We can parent our own QMenu's to this guy, instead of using nukes built-in
    menu commands.
    '''

    from Qt import QtWidgets
    for widget in QtWidgets.QApplication.instance().allWidgets():
        if isinstance(widget, QtWidgets.QMenuBar):
            return widget


def setup_construct_menu():
    '''Setup Construct Action menu'''
    from construct_ui.menus import ActionMenu

    menubar = get_nuke_menubar()
    menubar.addMenu(ActionMenu('Construct', menubar))
