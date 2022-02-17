.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

======================
collective.filterednav
======================

This is a trivial package that does one thing: provide folder listings that exclude items marked exclude_from_nav.

This depends on the existence of a field index for exclude_from_nav.
This does not exist in default Plone and must be added via the portal_catalog tool or equivalent setup.
If there is no such index, folder listings are unfiltered.

It's currently only meant to work with Plone 5.1.x.

Installation
------------

Install collective.filterednav by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.filterednav


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.filterednav/issues
- Source Code: https://github.com/collective/collective.filterednav
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
