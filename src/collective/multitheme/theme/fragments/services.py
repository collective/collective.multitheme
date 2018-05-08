def folder_url(self):
	url = self.data['folder_url']
	return url

def item_width(self):
	images = self.data['image_items']
	return (100/images) - 1
