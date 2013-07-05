from Acquisition import aq_inner
from plone.app.contentlisting.interfaces import IContentListing
from plone.app.contentlisting.interfaces import IContentListingObject
from five import grok
from plone.directives import dexterity, form
from plone.memoize.view import memoize


from plone.namedfile.interfaces import IImageScaleTraversable


# Interface class; used to define content-type schema.
class IBiodiversityFactsheet(form.Schema, IImageScaleTraversable):
    """
    Factsheets with biodiversity info
    """


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.
class BiodiversityFactsheet(dexterity.Container):
    grok.implements(IBiodiversityFactsheet)
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# templates called biodiversityfactsheetview.pt .
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@view" appended unless specified otherwise
# using grok.name below.
# This will make this view the default view for your content-type

grok.templatedir('templates')


class BiodiversityFactsheetView(grok.View):
    grok.context(IBiodiversityFactsheet)
    grok.require('zope2.View')
    grok.name('view')

    @memoize
    def facts(self):
        context = aq_inner(self.context)
        sections = context.getFolderContents({'portal_type': 'Section'})
        fact_data = []
        for section in sections:
            data = {}
            data['object'] = IContentListingObject(section)
            section_object = data['object'].getObject()
            facts = section_object.getFolderContents({'portal_type': 'Fact'})
            data['facts'] = IContentListing(facts)
            fact_data.append(data)

        return fact_data
