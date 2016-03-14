# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t; python-indent: 4 -*-§
import logging

from core.extensions.extensions import IExtension
from core.processor.iprocessor import IProcessor


class MyFirstExtension(IExtension):
    def __init__(self):
        """
        init
        """
        # initialise parent class
        super().__init__()

    def activate(self):
        """
        On activation tell that this has been successfull.
        """
        # get the automatic procedure from IPlugin
        super().activate()
        return

    def deactivate(self):
        """
        On deactivation check that the 'activated' flag was on then
        tell everything's ok to the test procedure.
        """
        super().deactivate()

    def get_tasks(self):
        return [TestProcessor()]


class TestProcessor(IProcessor):
    def run(self):
        logging.warning("my test extension")
		