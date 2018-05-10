# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['Nuke']

from os.path import join, dirname, basename
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

    name = 'Nuke'
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
        return nuke.root().modified()

    def save_file(self, file):
        import nuke
        from construct_ui.dialogs import ask

        if self.modified():
            if ask('Unsaved changes', 'Would you like to save?'):
                nuke.scriptSave()

        nuke.scriptSaveAs(file)

    def open_file(self, file):
        import nuke
        nuke.scriptOpen(file)

    def get_selection(self):
        import nuke
        return nuke.selectedNodes()

    def set_selection(self, selection):
        import nuke
        for node in self.get_selection():
            node.setSelected(False)
        for node in selection:
            node.setSelected(True)

    def get_workspace(self):
        pass

    def set_workspace(self, directory):
        pass

    def get_filepath(self):
        import nuke
        return nuke.root().name()

    def get_filename(self):
        import nuke
        return basename(nuke.root().name())

    def get_frame_range(self):
        import nuke
        root = nuke.root()
        return root.firstFrame(), root.lastFrame()

    def set_frame_range(self, start_frame, end_frame):
        import nuke
        root = nuke.root()
        root.knob('first_frame').setValue(start_frame)
        root.knob('last_frame').setValue(end_frame)

    def get_qt_parent(self):
        from Qt import QtWidgets
        app = QtWidgets.QApplication.instance()

        for widget in app.topLevelWidgets():
            if isinstance(widget, QtWidgets.QMainWindow):
                return widget
