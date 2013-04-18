from interfaces import ICarouselPortlet

from plone.app.portlets.portlets import base

from zope.interface import implements


class CarouselPortletAssignment(base.Assignment):
    implements(ICarouselPortlet)

    automatic_rotation = True
    title = ''
