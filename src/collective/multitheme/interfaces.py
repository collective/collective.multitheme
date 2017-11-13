# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

#import here or from __init.py ?
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.multitheme')


class ICollectiveMultithemeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectiveMultiThemeSettings(form.Schema):
	"""Adds settings to medialog.controlpanel
	"""

	form.fieldset(
		'Multitheme',
		label=_(u'Multitheme'),
		fields=[
			'style',
			'rules',
		],
	)

	style = schema.Choice(
        title=_(u"Style"),
	       values=['blue',
                   'dutchblue',
                   'red',
                   'ploneconf',
                   'booster',
                   'scheme1'],
        	required=True,
        )

	rules = schema.Choice(
            title=_(u"Layout Rules"),
            values=['rules', ],
            required=True,
    )

alsoProvides(ICollectiveMultiThemeSettings, IMedialogControlpanelSettingsProvider)
