# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
import os
from plone.app.textfield.value import RichTextValue

def post_install(context):
    """add front-page script"""
    #Add front page
    portal = api.portal.get()
    _create_frontpage(portal)


def install_demo_content(context):
    """add content script"""
    #Add demo content
    portal = api.portal.get()
    _create_content(portal)

def _create_frontpage(portal):

    if not portal.get('forside', False):
        portal_url = api.portal.get().absolute_url()
        body = """<p> </p>
            <p>This is a theming product for Plone 5</p>

            <h2>First steps</h2>
            <p><i>To set up your site, you might want to do the following:</i></p>
            <ul>
            <li>Reload the page to show the videos</li>
            <li><a href="%(portal_url)s/prefs_install_products_form">Install the theme if you have not done it already</a></li>
            <li><a href="%(portal_url)s/@@mail-controlpanel">Configure E-mail</a></li>
            <li><a href="%(portal_url)s/@@@@site-controlpanel">Configure Site and thumb settings</a><br/>
                Note: You can aloschange the logo</li>
            <li><a href="%(portal_url)s/prefs_install_products_form">Install demo content to play around with (chose Multitheme Demo Content profile)</a>.</li>
            </ul>
            <h2>Configuring the theme</h2>
            <p>Colors and layout can be configured, so do th following:</p>
            <ul>
            <li><a href="%(portal_url)s/@@medialog_controlpanel">Configure Settings in (Medialog) Site Control Panel</a>-.
            <br/>Note: Some layouts will not be finishde before I get some help… </li>
            <li><a href="%(portal_url)s/test_rendering">See a test rendering</a></li>
            <li>Repeat</li>
            </ul>
            <p><iframe width="840" height="473"
                src="https://www.youtube.com/embed/DF8d7DNGG4g?rel=0&amp;showinfo=0"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
                </iframe>
            </p>

            <p> </p>
            <h2>Changing the theme colors</h2>
            <p><iframe width="840" height="473"
                src="https://www.youtube.com/embed/FinvAN2IVcI?rel=0&amp;controls=0&amp;showinfo=0"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
                </iframe>
            </p>
            <p> </p>
            <h2>Using the theme fragments</h2>
            <ul>
            <li>Set the view on a folder to 'Mosaic Layout'</li>
            <li>Edit that page, Customize the layout by adding Themefragments from [Insert] Themefragments</li>
            <li>If you are lucky, you can see most of the fragments here: http://xweb14d.plana.dk:8081/Plone/fragments</li>
            </ul>
                <p><iframe width="840" height="473"
                src="https://www.youtube.com/embed/C2NDUJK7vZ0?rel=0&amp;controls=0&amp;showinfo=0"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
                </iframe>
            </p>
            <p> </p>
            <h2>Customizing the tiles</h2>
            <ul>
                <li>There is a new visual tile selector. <br/>
                The images nees to have the same name as the fragment, but ending with '.png' instead of '.pt'</li>
                <li>In manifest.cfg you can customize the names of the tiles</li>
                <li>If you name the fragment 'Hidden: somefragent name' it will not show up in Mosaic</li>
                <li>Currently, these fragments are hidden<br/>
                  <ul><li>fullpage_menu: Not finisehd</li>
                    <li>header: Rare use cases (needed if we manage to get site layouts)</li>
                    <li>livesearch: (not working proplerly)</li>
                    <li>richtext_block: Quite similar to normal rich text tile</li>
                    <li>richtext_list: Not finished</li>
                    <li>socialtop: Update of Plone (to 5.1) gives error on 'mail settings'</li>
                    <li>structure_abovecontent: Rare use cases (like site layout)</li>
                    <li>structure_abovecontentttitle: Rare use cases (like site layout)</li>
                    <li>structure_belowcontentbody: Rare use cases (like site layout)</li>
                    <li>testing = Hidden: testing</li>
                    <li>textlogo: Rare use cases (like site layout)</li>
                    <li>upload = Not working yet</li>
                    <li>webcoutier_global_nav = Rare use case s(like site layout)</li>
                    <li>xxxx = Hidden xxx</li>
                  </ul>
                </li>
            </ul>
            <p> </p>
            <p><iframe width="840" height="473"
                src="https://www.youtube.com/embed/Kr98zm3K3Vk?rel=0&amp;controls=0&amp;showinfo=0"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
            </iframe>
            </p>
            <p> </p>""" % {'portal_url': portal_url}

        forside = api.content.create(
            type='Document',
            container=portal,
            title=u'Multi Theme',
            description=u'A Plone 5 theme ',
            id='forside',
            text = RichTextValue(
            body,
			'text/html',
            'text/x-html-safe'
            )
        )

    	api.content.transition(obj=forside, transition='publish')
    	portal.default_page = "forside"


def _create_content(portal):

    if not portal.get('slider', False):
        slider = api.content.create(
            type='Folder',
            container=portal,
            title=u'Slider',
            id='slider',
        )

        titles = ['Image', 'Elephants', 'Cape Town', 'Japan', 'Malaysia', 'Argentina', 'Ivory Coast' ]
        for slider_number in range(1, 4):
            slider_name = u'slider-{0}'.format(str(slider_number))
            slider_image = api.content.create(
                type='Image',
                container=slider,
                id=slider_name,
                title=titles[slider_number],
                description=u'EMN 2012-2013'
            )
            slider_image.image = load_image(slider_number)
        api.content.transition(obj=slider, transition='publish')


    if not portal.get('portfolio', False):
        portfolio = api.content.create(
            type='Folder',
            container=portal,
            title=u'Portfolio',
            id='portfolio',
        )

        titles = ['Image', 'Elephants', 'Cape Town', 'Japan', 'Malaysia', 'Argentina', 'Ivory Coast' ]
        for slider_number in range(1, 7):
            slider_name = u'slider-{0}'.format(str(slider_number))
            slider_image = api.content.create(
                type='Image',
                container=portfolio,
                id=slider_name,
                title=titles[slider_number],
                description=u'EMN 1992-2013'
            )
            slider_image.image = load_image(slider_number)
        api.content.transition(obj=portfolio, transition='publish')


    if not portal.get('features', False):
        features = api.content.create(
            type='Folder',
            container=portal,
            title=u'Features',
            description=u"""Including all bolts and nuts.
            	All content in folder 'features' will show here.
            	To choose icon you will have to enable iconpicker behavior for your content type
            	in the Dexterity content type control panel""",
            id='features'
        )

        icons = ['fa-group', 'fa-heart', 'fa-home', 'fa-lock', 'fa-leaf', 'fa-key', 'fa-sitemap']
        titles = ['Clean', 'Fresh', 'Modern', 'Buzzword', 'Responsive', 'Safe', 'Grieg Medialog']
        for page_number in range(1, 7):
            page_name = u'page-{0}'.format(str(page_number))
            new_page = api.content.create(
                type='Document',
                container=features,
                id=page_name,
                title=titles[page_number],
                iconfield=icons[page_number],
                countto = page_number * 100,
                description='Lorem ipsum dolor sit amet, consectetur adipisicing elit',
            )
            api.content.transition(obj=new_page, transition='publish')
        api.content.transition(obj=features, transition='publish')

    if not portal.get('morefeatures', False):
        morefeatures = api.content.create(
            type='Folder',
            container=portal,
            title=u'More Features',
            description=u"""In another folder, '/morefeatures'""",
            id='morefeatures'
        )

        icons = ['fa-lock', 'fa-leaf', 'fa-key', 'fa-sitemap']
        titles = ['Buzzword', 'Responsive', 'Safe', 'Grieg Medialog']
        for page_number in range(1, 4):
            page_name = u'feature-{0}'.format(str(page_number))
            new_page = api.content.create(
                type='Document',
                container=morefeatures,
                id=page_name,
                title=titles[page_number],
                iconfield=icons[page_number],
                description='These are in the moreffeature folder',
            )
            api.content.transition(obj=new_page, transition='publish')
        api.content.transition(obj=morefeatures, transition='publish')


    if not portal.get('services', False):
        services = api.content.create(
            type='Folder',
            container=portal,
            title=u'Services',
            description=u"""We can do everything!
            	Save news items or other content with image in folder 'services'""",
            id='services'
        )

        titles = ['Fancy', 'Fast', 'SEO','Grieg Medialog']
        for page_number in range(1, 4):
            page_name = u'news-{0}'.format(str(page_number))
            new_page = api.content.create(
                type='News Item',
                container=services,
                id=page_name,
                title=titles[page_number],
                description='Lorem ipsum dolor sit amet, consectetur adipisicing elit',
            )
            new_page.image = load_image(page_number)
            api.content.transition(obj=new_page, transition='publish')
        api.content.transition(obj=services, transition='publish')

    if not portal.get('moreservices', False):
        moreservices = api.content.create(
            type='Folder',
            container=portal,
            title=u'More Services',
            description=u"""We can do everything, again!
            	Save news items or other content with image in folder 'moreservices'""",
            id='moreservices'
        )

        titles = ['Fancy', 'Fast', 'SEO','Grieg Medialog']
        for page_number in range(1, 4):
            page_name = u'news-{0}'.format(str(page_number))
            new_page = api.content.create(
                type='News Item',
                container=moreservices,
                id=page_name,
                title=titles[page_number],
                description='Lorem ipsum dolor sit amet, consectetur adipisicing elit',
            )
            new_page.image = load_image(page_number)
            api.content.transition(obj=new_page, transition='publish')
        api.content.transition(obj=moreservices, transition='publish')

def load_image(slider):
    from plone.namedfile.file import NamedBlobImage
    filename = os.path.join(os.path.dirname(__file__), 'theme', 'img',
                            'slide-{0}.jpg'.format(slider))
    return NamedBlobImage(
        data=open(filename, 'r').read(),
        filename=u'slide-{0}.jpg'.format(slider)
    )


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
