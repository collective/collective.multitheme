.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.multitheme
==============================================================================

A theme for Plone 5

Features
--------

- A theme for Plone 5 that can be customized.
- Choose between 'themes' in the control panel
- Choose between fragment tiles in the Mosaic Layout editor
- Choose between (layout) styles for each Mosaic Fragment Tile


Documentation
-------------

No documentation yet


Translations
------------

This product has not been translated yet


Installation
------------

Install collective.multitheme by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.multitheme


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.multitheme/issues
- Source Code: https://github.com/collective/collective.multitheme
- Use  'lessc mylessfile.less mycssfile.css'


Lessc
-------

If you change settings / colors, run this:


cd blue; lessc theme.less  theme.css;
cd ../blue; lessc theme.less  theme.css;
cd ../ploneconf; lessc theme.less  theme.css;
cd ../booster; lessc theme.less  theme.css;
cd ../red; lessc theme.less  theme.css;
cd ../spot; lessc theme.less  theme.css;
cd ../dutchblue; lessc theme.less  theme.css;
cd ../scheme1; lessc theme.less  theme.css;


License
-------

The project is licensed under the GPLv2.
