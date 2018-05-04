# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['Nuke']

from os.path import join, dirname
from construct.extension import HostExtension
from construct_nuke.tasks import (
    setup_construct_nuke
)


class Nuke(HostExtension):
    '''Construct Nuke integration'''

    name = 'Nuke'
    attr_name = 'nuke'

    def available(self, ctx):
        return True

    def load(self):

        self.add_template_path(join(dirname(__file__), 'templates'))

        # Extend cpenv_launcher to activate cpenv modules before launch
        from construct_launcher.constants import BEFORE_LAUNCH

        self.add_task(
            'launch.nuke*',
            setup_construct_nuke,
            priority=BEFORE_LAUNCH
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
        import nuke
        # clear selection
        for node in self.get_selection():
            node.setSelected(False)

        # set new selection
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
        return os.path.dirname(nuke.root().name())

    def get_frame_range(self):
        import nuke
        return nuke.root().firstFrame(), nuke.root().lastFrame()

    def set_frame_range(self, start_frame, end_frame):
        import nuke
        pass

    def get_qt_parent(self, widget_cls=None):
        return None

    def get_qt_loop(self):
        from Qt import QtWidgets
        return QtWidgets.QApplication.instance()
