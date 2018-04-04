# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.filterednav.testing import COLLECTIVE_FILTEREDNAV_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.filterednav is properly installed."""

    layer = COLLECTIVE_FILTEREDNAV_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.filterednav is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.filterednav'))

    def test_browserlayer(self):
        """Test that ICollectiveFilterednavLayer is registered."""
        from collective.filterednav.interfaces import (
            ICollectiveFilterednavLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveFilterednavLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FILTEREDNAV_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.filterednav'])

    def test_product_uninstalled(self):
        """Test if collective.filterednav is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.filterednav'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveFilterednavLayer is removed."""
        from collective.filterednav.interfaces import \
            ICollectiveFilterednavLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveFilterednavLayer,
           utils.registered_layers())
