# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.filterednav


class CollectiveFilterednavLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.filterednav)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.filterednav:default')


COLLECTIVE_FILTEREDNAV_FIXTURE = CollectiveFilterednavLayer()


COLLECTIVE_FILTEREDNAV_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FILTEREDNAV_FIXTURE,),
    name='CollectiveFilterednavLayer:IntegrationTesting'
)


COLLECTIVE_FILTEREDNAV_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_FILTEREDNAV_FIXTURE,),
    name='CollectiveFilterednavLayer:FunctionalTesting'
)


COLLECTIVE_FILTEREDNAV_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_FILTEREDNAV_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveFilterednavLayer:AcceptanceTesting'
)
