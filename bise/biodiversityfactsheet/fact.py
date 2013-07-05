from zope.app.container.interfaces import IObjectAddedEvent
from five import grok
from plone.directives import dexterity, form

from plone.namedfile.interfaces import IImageScaleTraversable


# Interface class; used to define content-type schema.
class IFact(form.Schema, IImageScaleTraversable):
    """
    Factsheet content
    """


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.
class Fact(dexterity.Container):
    grok.implements(IFact)
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# templates called factview.pt .
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@view" appended unless specified otherwise
# using grok.name below.
# This will make this view the default view for your content-type

grok.templatedir('templates')


class FactView(grok.View):
    grok.context(IFact)
    grok.require('zope2.View')
    grok.name('view')


@grok.subscribe(IFact, IObjectAddedEvent)
def exclude_from_nav(context, event):
    context.exclude_from_nav = True
