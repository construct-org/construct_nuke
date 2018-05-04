# -*- coding: utf-8 -*-
from __future__ import absolute_import


def get_top_level_widget(widget_cls=None):
    from Qt import QtWidgets
    widget_cls = widget_cls or QtWidgets.QWidget
    for widget in QtWidgets.QApplication.instance().topLevelWidgets():
        if isinstance(widget, widget_cls):
            return widget


def get_nuke_menubar():
    from Qt import QtWidgets
    for widget in QtWidgets.QApplication.instance().allWidgets():
        if isinstance(widget, QtWidgets.QMenuBar):
            return widget
