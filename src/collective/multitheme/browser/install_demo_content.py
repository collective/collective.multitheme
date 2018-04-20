# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.protect import protect

from collective.multitheme import  _

class InstallDemoContent(BrowserView):
    """ Install demo contents."""

    def __call__(self, *args, **kw):
        setup_tool = getToolByName(self.context, 'portal_setup')
        plone_utils = getToolByName(self.context, 'plone_utils')
        setup_tool.runAllImportStepsFromProfile('profile-collective.multitheme:democontent')
        #self.context.plone_utils.addPortalMessage(_(u'Demo content was installed.'), 'info')
