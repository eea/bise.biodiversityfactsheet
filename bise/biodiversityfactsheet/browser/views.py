from Acquisition import aq_inner
from bise.biodiversityfactsheet.fact import IBasicFact
from plone.app.contentlisting.interfaces import (IContentListing,
                                                 IContentListingObject)
from plone.dexterity.browser import edit
from plone.memoize.view import memoize
from Products.Five.browser import BrowserView

# from z3c.form.field import Fields
# from zope import schema


class BiodiversityFactsheetView(BrowserView):

    @memoize
    def facts(self):
        context = aq_inner(self.context)
        sections = context.getFolderContents({'portal_type': 'Section'})
        fact_data = []

        targets = self.request.form.get('targets', '')

        for section in sections:
            data = {}
            data['object'] = IContentListingObject(section)
            section_object = data['object'].getObject()
            facts = section_object.getFolderContents({'portal_type': 'Fact'})
            fact_list = []

            if targets == "":
                fact_list = facts
                data['facts'] = IContentListing(fact_list)
                fact_data.append(data)
            else:
                if section_object.Title() == "General information":
                    fact_list = facts
                    data['facts'] = IContentListing(fact_list)
                    fact_data.append(data)
                else:
                    for fact in facts:
                        targetsArray = targets.split(",")

                        if fact.getObject().targets is not None:
                            for target in targetsArray:
                                if target in fact.getObject().targets:
                                    fact_list.append(fact)

                    if len(fact_list) > 0:
                        data['facts'] = IContentListing(fact_list)
                        fact_data.append(data)

        return fact_data


class FactView(BrowserView):
    """ View a fact
    """


class FactRenderView(BrowserView):
    """ Render a fact. Returns a html fragment
    """

    def files(self):
        context = aq_inner(self.context)
        files = context.getFolderContents({'portal_type': 'File'})

        return IContentListing(files)

    def links(self):
        context = aq_inner(self.context)
        links = context.getFolderContents({'portal_type': 'Link'})

        return IContentListing(links)

    def getMapIds(self):
        context = aq_inner(self.context)

        return context.webmapid.split(",")


class SimpleFactEditForm(edit.DefaultEditForm):

    schema = IBasicFact
    additionalSchemata = ()
