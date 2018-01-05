from bise.biodiversityfactsheet import MessageFactory as _
from plone.directives import dexterity, form
from plone.namedfile.interfaces import IImageScaleTraversable
from zope import schema
from zope.interface import implements


class IBiodiversityFactsheet(form.Schema, IImageScaleTraversable):
    """ Factsheets with biodiversity info """

    fact_countryName = schema.Text(
        title=_(u'Country name'),
        description=_(u'Name of the country to use in the maps '),
        required=True,
        )
    fact_countryCode = schema.Text(
        title=_(u'Country code'),
        description=_(u'Two letter country code to use in the maps '),
        required=True,
        )
    fact_countryISOCode = schema.Text(
        title=_(u'Country ISO code'),
        description=_(u'Three letter country ISO code to use in the maps'),
        required=True,
        )


class BiodiversityFactsheet(dexterity.Container):
    implements(IBiodiversityFactsheet)
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# templates called biodiversityfactsheetview.pt .
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@view" appended unless specified otherwise
# using grok.name below.
# This will make this view the default view for your content-type

# grok.templatedir('templates')
