# -*- coding: utf-8 -*-
from i18n import MessageFactory as _
from interfaces import ICarouselPortlet
from plone.app.portlets.portlets import base
from plone.autoform.form import AutoExtensibleForm
from plone.memoize.view import memoize
from portlet import CarouselPortletAssignment
from Products.CMFPlone.utils import getFSVersionTuple
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.portlet.carousel.interfaces import ICarouselItem

import logging


logger = logging.getLogger('collective.portlet.carousel')
WIDGETS_1X = False
PLONE5 = getFSVersionTuple()[0] >= 5

if PLONE5:
    base_AddForm = base.AddForm
    base_EditForm = base.EditForm
else:
    # PLONE 4 Support:
    # Either Plone 4 plus compatible plone.app.widgets, or Plone 4.x without:
    from plone.app.portlets.browser import z3cformhelper
    from z3c.form import field
    try:
        class base_AddForm(AutoExtensibleForm, z3cformhelper.AddForm):
            pass

        class base_EditForm(AutoExtensibleForm, z3cformhelper.EditForm):
            pass

        WIDGETS_1X = True
    except ImportError:
        WIDGETS_1X = False
        base_AddForm = z3cformhelper.AddForm
        base_EditForm = z3cformhelper.EditForm


USE_AUTOFORM = PLONE5 or WIDGETS_1X



script = """
jQuery(function($){
  rotate = %(rotate)s;
  var timeout;

  next = function(index, auto) {
    clearTimeout(timeout);
    x = parseInt(index);
    p = $('.portletCarousel ul li');
    i = $('.portletCarousel dl dd.carouselPortletItem');
    p.removeClass('current');
    i.removeClass('current').animate({opacity:0});
    i.hide();
    x%%=i.length;
    ci = i.eq(x);
    cp = p.eq(x);
    cp.addClass('current');
    ci.addClass('current').animate({opacity:1});
    ci.show();
    if(auto) {
      timeout = setTimeout("next("+(++x)+", " + auto + ")", %(timeout)d);
    }
  }

  $('.portletCarousel ul li').click(function(){
    cp = $(this);
    if (cp.is('.current'))
      return false;
    x = cp.index('.portletCarousel ul li');
    next(x, true);
    return false;
  });

  if (rotate) {
    $(document).ready(function() {
      timeout = setTimeout("next(1,true)", %(timeout)d);
    });
  }

});


"""


class CarouselPortletRenderer(base.Renderer):
    render = ViewPageTemplateFile('portlet.pt')

    @property
    def title(self):
        return self.data.header

    @property
    def available(self):
        return self.data.collection_reference or \
            len(self.data.references) > 0

    @property
    def omit_border(self):
        return self.data.omit_border

    @property
    def rotate(self):
        return self.data.automatic_rotation and \
            len(self.items()) > 1 and self.timeout > 0

    @property
    def timeout(self):
        return self.data.timeout * 1000

    @memoize
    def items(self):
        items = []

        collection = None
        if self.data.collection_reference:
            collection = self.data.collection_reference.to_object

        if collection:
            if collection.portal_type == 'Folder':
                listing = collection.restrictedTraverse('@@folderListing', None)
                brains = tuple(listing({'object_provides': ICarouselItem.__identifier__}))
                for brain in brains:
                    items.append(brain.getObject())
            else:
                resf = hasattr(collection, 'results') and \
                    collection.results or collection.queryCatalog
                for brain in resf():
                    items.append(brain.getObject())
        else:
            references = self.data.references
            for reference in references:
                items.append(reference.to_object)

        if hasattr(self.data, 'limit') and self.data.limit > 0:
            return items[:self.data.limit]

        return items

    def script(self):
        return script % dict(rotate=self.rotate and 'true' or 'false',
                             timeout=self.timeout)


class CarouselPortletAddForm(base_AddForm):
    if USE_AUTOFORM:
        schema = ICarouselPortlet
    else:
        fields = field.Fields(ICarouselPortlet)

    label = _(u"Add carousel portlet")

    def create(self, data):
        return CarouselPortletAssignment(**data)


class CarouselPortletEditForm(base_EditForm):
    if USE_AUTOFORM:
        schema = ICarouselPortlet
    else:
        fields = field.Fields(ICarouselPortlet)

    label = _(u"Edit carousel portlet")
