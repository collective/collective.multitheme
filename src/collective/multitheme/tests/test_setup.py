# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.multitheme.testing import COLLECTIVE_MULTITHEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.multitheme is properly installed."""

    layer = COLLECTIVE_MULTITHEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.multitheme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.multitheme'))

    def test_browserlayer(self):
        """Test that ICollectiveMultithemeLayer is registered."""
        from collective.multitheme.interfaces import (
            ICollectiveMultithemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveMultithemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_MULTITHEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.multitheme'])

    def test_product_uninstalled(self):
        """Test if collective.multitheme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.multitheme'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveMultithemeLayer is removed."""
        from collective.multitheme.interfaces import \
            ICollectiveMultithemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveMultithemeLayer, utils.registered_layers())
