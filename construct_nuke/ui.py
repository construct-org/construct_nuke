# -*- coding: utf-8 -*-
from __future__ import absolute_import


def get_nuke_menubar():
    from Qt import QtWidgets
    for widget in QtWidgets.QApplication.instance().allWidgets():
        if isinstance(widget, QtWidgets.QMenuBar):
            return widget
