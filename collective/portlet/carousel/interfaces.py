from i18n import MessageFactory as _

from plone.directives import form
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.namedfile.field import NamedBlobImage
from plone.portlets.interfaces import IPortletDataProvider

from zope import schema
from zope.interface import alsoProvides, Interface

from z3c.relationfield.schema import RelationChoice, RelationList


class ICarouselItem(Interface):
    """ Marker inferface for item that it can be considered a carousel item """


class ICarouselItemBehavior(form.Schema, ICarouselItem):

    form.fieldset(
        'carousel',
        label=_('fieldset_carousel', default=u'Carousel'),
        fields=(
            'carousel_heading',
            'carousel_description',
            'carousel_background',
            'carousel_link',
        ),
    )

    carousel_heading = schema.TextLine(
        title=_(u"Carousel heading"),
        description=_(u"If this heading is not specified the title of the "
                      u"object will be used as heading"),
        required=False
    )

    carousel_description = schema.Text(
        title=_(u"Carousel description"),
        description=_(u"If this description is not specified the description "
                      u"of the object will be used as description"),
        required=False
    )

    carousel_background = NamedBlobImage(
        title=_(u"Carousel background"),
        description=_(u"This image is displayed in the top of the page "
                      u"for pages below this section"),
        required=False
    )

    carousel_link = RelationChoice(
        title=_(u"Carousel link"),
        description=_(u"If selected this link will be used from the carousel "
                      u"item, otherwise a link to this object is used."),
        required=False,
        source=ObjPathSourceBinder(),
    )


alsoProvides(ICarouselItemBehavior, form.IFormFieldProvider)


class ICarouselPortlet(IPortletDataProvider):
    title = schema.TextLine(
        title=_(u"Portlet header"),
    )

    collection_reference = RelationChoice(
        title=_(u"Collection reference"),
        description=_(u"Select the collection that should be used to fetch "
                      u"the elements that are shown in the carousel"),
        required=False,
        source=ObjPathSourceBinder(portal_type=['Collection']),
    )

    references = RelationList(
        title=_(u"References to elements"),
        description=_(u"If no collection is selected the following elements "
                      u"will be displayed in the carousel"),
        value_type=RelationChoice(
            required=False,
            source=ObjPathSourceBinder(
                object_provides=ICarouselItem.__identifier__
            ),
        ),
        required=False
    )

    limit = schema.Int(
        title=_(u"Number of elements to be shown in the carousel"),
        required=True,
    )

    automatic_rotation = schema.Bool(
        title=_(u"Automatic rotation"),
        required=False,
        default=True,
    )
