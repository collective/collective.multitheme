#Can not use this (unauthorized)
def sitetitle(self):
    from plone.api import portal
    return portal.getProperty('title')
