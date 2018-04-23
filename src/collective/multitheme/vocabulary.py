# -*- coding: utf-8 -*-
from AccessControl import getSecurityManager
from collective.themefragments.interfaces import FRAGMENTS_DIRECTORY
from collective.themefragments.traversal import ThemeFragment
from collective.themefragments.utils import cache
from collective.themefragments.utils import getFragmentsSettings
from os.path import splitext
from plone.app.blocks.layoutbehavior import ILayoutBehaviorAdaptable
from plone.app.blocks.layoutbehavior import LayoutAwareTileDataStorage
from plone.app.dexterity.permissions import GenericFormFieldPermissionChecker
from plone.app.theming.interfaces import THEME_RESOURCE_NAME
from plone.app.theming.utils import getCurrentTheme
from plone.app.theming.utils import isThemeEnabled
from plone.app.tiles.browser.add import DefaultAddForm
from plone.app.tiles.browser.add import DefaultAddView
from plone.app.tiles.browser.edit import DefaultEditForm
from plone.app.tiles.browser.edit import DefaultEditView
from plone.app.vocabularies.catalog import CatalogSource as CatalogSourceBase
from plone.memoize.view import memoize
from plone.resource.utils import queryResourceDirectory
from plone.supermodel import model
from plone.supermodel.interfaces import ISchemaPolicy
from plone.supermodel.parser import DefaultSchemaPolicy
from plone.supermodel.parser import parse
from plone.tiles.absoluteurl import TransientTileAbsoluteURL
from plone.tiles.data import decode
from plone.tiles.data import defaultTileDataStorage
from plone.tiles.data import encode
from plone.tiles.data import TransientTileDataManager
from plone.tiles.esi import ESI_TEMPLATE
from plone.tiles import Tile
from plone.tiles.interfaces import ESI_HEADER
from plone.tiles.interfaces import IESIRendered
from plone.tiles.interfaces import ITileDataManager
from plone.tiles.interfaces import ITileDataStorage
from plone.z3cform.fieldsets.group import Group
from z3c.form.form import Form
from zExceptions import Unauthorized
from zope.component import adapter
from zope.globalrequest import getRequest
from zope.i18nmessageid import MessageFactory
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import noLongerProvides
from zope.interface import Interface
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import json
import logging

_ = MessageFactory('collective.themefragments')

logger = logging.getLogger('collective.themefragments')




class TileCatalogSource(CatalogSourceBase):
    """Catalog source, which falsely claims to include everything, because
    otherwise tile data with broken references cannot be deserialized
    (because broken reference would not be found from catalog source).
    """
    def __contains__(self, value):
        return True  # Always contains to allow lazy handling of removed objs


CatalogSource = TileCatalogSource()


@implementer(IVocabularyFactory)
class ThemeFragmentsTilesVocabularyFactory(object):
    """Return vocabulary of available theme fragments to be used as tiles"""

    @cache('vocabulary')
    def __call__(self, context=None):
        request = getRequest()

        if not isThemeEnabled(request):
            return SimpleVocabulary([])

        currentTheme = getCurrentTheme()
        if currentTheme is None:
            return SimpleVocabulary([])

        themeDirectory = queryResourceDirectory(THEME_RESOURCE_NAME, currentTheme)  # noqa
        if themeDirectory is None:
            return SimpleVocabulary([])

        if not themeDirectory.isDirectory(FRAGMENTS_DIRECTORY):
            return SimpleVocabulary([])

        # Get settings to map titles
        titles = getFragmentsSettings(themeDirectory, 'themefragments:tiles')

        tiles = [splitext(filename)[0] for filename
                 in themeDirectory[FRAGMENTS_DIRECTORY].listDirectory()
                 if splitext(filename)[-1] == '.pt' and
                 themeDirectory[FRAGMENTS_DIRECTORY].isFile(filename)]

        terms = [SimpleTerm(None, '', _(u'-- select fragment --'))]
        for tile in tiles:
            title = titles.get(tile, None)
            title = title is None and tile or title.strip().split('#')[0]
            if title:
                if title[0].isupper():
                    terms.append(SimpleTerm(tile, tile, title))
        return SimpleVocabulary(terms)
