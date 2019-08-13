# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['Nuke']

import os
from os.path import join, dirname, basename
import construct
from construct.extension import HostExtension
from construct_nuke.tasks import (
    setup_construct_nuke
)
from construct_launcher.constants import BEFORE_LAUNCH


class Nuke(HostExtension):
    '''Construct Nuke Host Extension

    Implements the HostExtension Interface. Provides a default nuke workspace
    template and a launch task.
    '''

    name = 'nuke'
    attr_name = 'nuke'

    def available(self, ctx):
        return True

    def load(self):

        self.add_template_path(join(dirname(__file__), 'templates'))
        self.add_task(
            'launch.nuke*',
            setup_construct_nuke,
            priority=BEFORE_LAUNCH
        )

    def modified(self):
        import nuke
        return (
            nuke.root().modified() and
            self.get_filename() != 'Root'
        )

    def save_file(self, file):
        import nuke
        nuke.scriptSaveAs(file)

    def open_file(self, file):
        import nuke
        nuke.scriptOpen(file)

    def get_selection(self):
        import nuke
        return nuke.selectedNodes()

    def set_selection(self, selection):
        for node in self.get_selection():
            node.setSelected(False)
        for node in selection:
            node.setSelected(True)

    def get_workspace(self):
        import nuke
        return nuke.root()['project_directory'].getValue()

    def set_workspace(self, directory):
        import nuke
        from construct_ui import resources

        ctx = construct.get_context()
        fav_icon = resources.path(':/brand/construct_icon-white-on-black')
        favs = ['project', 'sequence', 'shot', 'asset', 'workspace']

        for fav in favs:
            fav_name = fav.title()
            nuke.removeFavoriteDir(fav_name)

            entry = ctx[fav]
            if entry:
                directory = entry.path
                nuke.addFavoriteDir(
                    fav_name,
                    directory=directory,
                    type=(nuke.IMAGE | nuke.SCRIPT | nuke.GEO),
                    icon=fav_icon,
                    tooltip=directory
                )

        os.chdir(directory)
        nuke.root()['project_directory'].setValue(directory)

    def get_filepath(self):
        import nuke
        return nuke.root().name()

    def get_filename(self):
        import nuke
        return basename(nuke.root().name())

    def get_frame_range(self):
        import nuke
        viewer = nuke.activeViewer().node()
        viewer_range = viewer.knob('frame_range').getValue()
        start, end = [int(v) for v in viewer_range.split('-')]
        root = nuke.root()
        min = root.firstFrame()
        max = root.lastFrame()
        return min, start, end, max

    def set_frame_range(self, min, start, end, max):
        import nuke
        root = nuke.root()
        root.knob('first_frame').setValue(min)
        root.knob('last_frame').setValue(max)
        viewer = nuke.activeViewer().node()
        viewer['frame_range'].setValue('%d-%d' % (start, end))
        viewer['frame_range_lock'].setValue(True)

    def get_frame_rate(self):
        import nuke
        root = nuke.root()
        return root.knob('fps').getValue()

    def set_frame_rate(self, fps):
        import nuke
        root = nuke.root()
        return root.knob('fps').setValue(fps)

    def get_qt_parent(self):
        from Qt import QtWidgets
        app = QtWidgets.QApplication.instance()

        for widget in app.topLevelWidgets():
            if isinstance(widget, QtWidgets.QMainWindow):
                return widget
