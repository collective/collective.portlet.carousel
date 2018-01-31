from i18n import MessageFactory as _
from interfaces import ICarouselPortlet
from plone.app.portlets.portlets import base
from zope.interface import implements


class CarouselPortletAssignment(base.Assignment):
    implements(ICarouselPortlet)

    header = ''
    collection_reference = None
    references = []
    limit = 5
    automatic_rotation = True
    omit_border = False
    timeout = 8
    carousel_extlink = ''

    def __init__(self, header=u"", collection_reference=None, references=[],
                 limit=5, automatic_rotation=True,
                 omit_border=False, timeout=8,
                 carousel_extlink=''):
        self.header = header
        self.collection_reference = collection_reference
        self.references = references
        self.limit = limit
        self.automatic_rotation = automatic_rotation
        self.omit_border = omit_border
        self.timeout = timeout
        self.carousel_extlink = carousel_extlink

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave or
        static string if title not defined.
        """
        return self.header or _(u'portlet_carousel',
                               default=u"Carousel Portlet")
