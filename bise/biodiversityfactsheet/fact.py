from bise.biodiversityfactsheet import MessageFactory as _
from plone.app.textfield import RichText
from plone.directives import dexterity, form
from plone.namedfile.interfaces import IImageScaleTraversable
from zope import schema
from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

fact_icons = SimpleVocabulary(
    [
     SimpleTerm(value=u'text', title=_(u'Text')),
     SimpleTerm(value=u'map', title=_(u'Map')),
     SimpleTerm(value=u'link', title=_(u'Link')),
     SimpleTerm(value=u'graph', title=_(u'Graph')),
     SimpleTerm(value=u'pdf', title=_(u'PDF')),
     ]
    )


# Interface class; used to define content-type schema.
class IFact(form.Schema, IImageScaleTraversable):
    """
    Factsheet content
    """

    text = RichText(
        title=_(u'Text'),
        description=_(u'Text of this fact'),
        required=False,
        )

    embed = schema.Text(
        title=_(u'Embed code'),
        description=_(u'Paste here content coming from external site. '
                      u'Such as iframe, object, or other external site code.'),
        required=False,
        )

    webmapid = schema.Text(
        title=_(u'Webmap ID'),
        description=_(u'Webmap id(s) separated by commas'),
        required=False,
        )

    fact_icon = schema.Choice(
        title=_(u'Icon to show next to the title'),
        vocabulary=fact_icons,
        default=u'text',
        required=True
        )
    fact_source = RichText(
        title=_(u'Source'),
        description=_(u'Source'),
        required=True,
        )
    fact_year = schema.Text(
        title=_(u'Year'),
        description=_(u'Year'),
        required=True,
        )


class Fact(dexterity.Container):
    implements(IFact)


def exclude_from_nav(obj, event):
    obj.exclude_from_nav = True
