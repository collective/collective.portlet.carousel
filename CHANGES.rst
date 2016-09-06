Changelog
=========

1.1 (UNRELEASED)
----------------

Features:

- add option to specify an external uri in portlet.
  External link will override reference.
  [tmog]

- add option to set timeout in portlet.
  [tmog]

- add new widgets from plone.app.widgets
  [datakurre]

Fixes:

- use empty string as default for relation choices fixing an
  issue with the form library for non-required fields.
  [malthe]

- only do rotation if we have more
  than one item
  [tmog]

- allow picking old style Topics
  [tmog]

- add BBB for ATTopic
  [tmog]

- add Finnish localization
  [datakurre]


1.0 (30-12-2013)
----------------

Initial public release

Fixes:

- included the plone.behavior meta.zcml file,
  so that we get access to the <plone:behavior /> ZCML directive.
  [bogdangi]
- work with plone:master p.a.portlets
  [tmog]
