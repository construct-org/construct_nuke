# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['Nuke']

from os.path import join, dirname
from construct.extension import Extension
from construct_nuke.tasks import (
    setup_construct_nuke
)


class Nuke(Extension):
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
