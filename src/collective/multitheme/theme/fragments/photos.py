# -*- coding: utf-8 -*-
from zope import schema
from plone.app.contenttypes import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile import field as namedfile
from plone.namedfile.field import NamedImage
from plone.supermodel import model
from plone.directives import form
from zope.interface import provider

from plone.formwidget.multifile import MultiFileFieldWidget

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.photosbehavior')

from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow

from z3c.form.browser.multi import MultiWidget

@provider(IFormFieldProvider)
class IPhotosBehavior(form.Schema):
    """Adds settings to medialog.controlpanel
        """
    photos = schema.List(
        title = _(u"Images"),
        value_type=namedfile.NamedBlobImage(
        title = _(u"Image"),
        required=False)
    )

    form.widget(photos=MultiFileFieldWidget)
