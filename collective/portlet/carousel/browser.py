
from interfaces import ICarouselPortlet
from portlet import CarouselPortletAssignment
from i18n import MessageFactory as _

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets.portlets import base
from plone.app.portlets.browser import z3cformhelper

from z3c.form import field


class CarouselPortletRenderer(base.Renderer):
    render = ViewPageTemplateFile('portlet.pt')

    @property
    def title(self):
        return self.context.data.title

    @property
    def available(self):
        return self.context.data.collection_reference or \
            len(self.context.data.references) > 0

    @property
    def omit_border(self):
        return self.context.data.omit_border

    @property
    def rotate(self):
        return self.context.data.automatic_rotation

    def items(self):
        items = []

        collection = None
        if self.context.data.collection_reference:
            collection = self.context.data.collection_reference.to_object

        if collection:
            for brain in collection.results():
                items.append(brain.getObject())
        else:
            references = self.context.data.references
            for reference in references:
                items.append(reference.to_object)

        if hasattr(self.context.data, 'limit') and self.context.data.limit > 0:
            return items[:self.context.data.limit]

        return items


class CarouselPortletAddForm(z3cformhelper.AddForm):
    fields = field.Fields(ICarouselPortlet)
    label = _(u"Add carousel portlet")

    def create_assignment(self, data):
        return CarouselPortletAssignment(**data)


class CarouselPortletEditForm(z3cformhelper.EditForm):
    fields = field.Fields(ICarouselPortlet)
    label = _(u"Edit carousel portlet")
