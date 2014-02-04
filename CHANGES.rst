Changelog
=========

1.1 (UNRELEASED)
----------------

Features:

- add option to set timeout in portlet.
  [tmog]

Fixes:

- only do rotation if we have more
  than one item
  [tmog]

- allow picking old style Topics
  [tmog]

- add BBB for ATTopic
  [tmog]


1.0 (30-12-2013)
----------------

Initial public release

Fixes:

- included the plone.behavior meta.zcml file,
  so that we get access to the <plone:behavior /> ZCML directive.
  [bogdangi]
- work with plone:master p.a.portlets
  [tmog]
