
from interfaces import ICarouselPortlet
from portlet import CarouselPortletAssignment
from i18n import MessageFactory as _

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets.portlets import base
from plone.app.portlets.browser import z3cformhelper
from plone.memoize import ram

from z3c.form import field


class CarouselPortletRenderer(base.Renderer):
    render = ViewPageTemplateFile('portlet.pt')

    def title(self):
        return self.context.data.title

    @property
    def available(self):
        return True

    @property
    def rotate(self):
        return self.context.data.automatic_rotation

    def getItems(self):
        items = []

        collection = None
        if hasattr(self.context.data, 'collection_reference') and \
                self.context.data.collection_reference:
            collection = self.context.data.collection_reference.to_object

        if collection:
            for brain in collection.results():
                items.append(brain.getObject())
        else:
            references = self.context.data.references
            for reference in references:
                items.append(reference.to_object)

        return items


class CarouselPortletAddForm(z3cformhelper.AddForm):
    fields = field.Fields(ICarouselPortlet)
    label = _(u"Add carousel portlet")

    def create_assignment(self, data):
        return CarouselPortletAssignment(**data)


class CarouselPortletEditForm(z3cformhelper.EditForm):
    fields = field.Fields(ICarouselPortlet)
    label = _(u"Edit carousel portlet")
