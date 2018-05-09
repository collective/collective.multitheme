def get_wallitems(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()

def relocate_to(self):
    url = self.data['relocate_to']
    return url
