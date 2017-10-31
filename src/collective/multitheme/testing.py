# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.multitheme


class CollectiveMultithemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.multitheme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.multitheme:default')


COLLECTIVE_MULTITHEME_FIXTURE = CollectiveMultithemeLayer()


COLLECTIVE_MULTITHEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_MULTITHEME_FIXTURE,),
    name='CollectiveMultithemeLayer:IntegrationTesting'
)


COLLECTIVE_MULTITHEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_MULTITHEME_FIXTURE,),
    name='CollectiveMultithemeLayer:FunctionalTesting'
)


COLLECTIVE_MULTITHEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_MULTITHEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveMultithemeLayer:AcceptanceTesting'
)
