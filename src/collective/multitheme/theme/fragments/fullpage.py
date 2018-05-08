def get_wallitems(self):
    linked = self.data['linked_folder']
    folder = self.context.portal_catalog(UID=linked)
    return folder[0].getObject()

def relocate_to(self):
    linked = self.data['relocate_to']
    linked_d = self.context.portal_catalog(UID=linked)
    return linked_d[0].getObject()
