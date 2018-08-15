# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.CMFPlone.utils import getSiteLogo
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import ISiteSchema

class MenuViewlet(GlobalSectionsViewlet):
    """ A viewlet which renders the menu."""

    @property
    def logo_title(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ISiteSchema,
                                     prefix="plone",
                                     check=False)
        return settings.site_title

    @property
    def img_src(self):
        return  getSiteLogo()


#class TopViewlet(LanguageSelectorViewlet):
#    """ A viewlet which renders site links, flags, subsite chooser etc"""

#class FooterViewlet(GlobalSectionsViewlet):
#    """ A viewlet which renders the footer. Menu items can be defined in the control panel """
