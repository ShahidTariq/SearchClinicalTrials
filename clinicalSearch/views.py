from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import Context, loader
import xml.etree.ElementTree as ET
import datetime
from . models import ClinicalStudy,Condition,Outcome

import os

class Index(View):

    def post(self, request):
        pass

    def get(self, request):
        template = loader.get_template('clinicalSearch/index.html')
        tree = ET.parse(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'media/NCT00001193.xml'))
        root = tree.getroot()
        # open a file for writing

        resident_head = []

        count = 0
        cites_list = []
        pmid_list = []

        # for elt in tree.iter():
        #    print("%s: '%s'" % (elt.tag, elt.text))


        #create model instance
        clinicalSerachModel=ClinicalStudy()


        #insert org_id
        for data in root.findall('id_info'):
            clinicalSerachModel.org_study_id=data.find('org_study_id').text
            clinicalSerachModel.nct_id = data.find('nct_id').text

        #insert official title,source
        official_title = root.find('official_title').text
        clinicalSerachModel.official_title=official_title
        clinicalSerachModel.source = root.find('source').text
        clinicalSerachModel.overall_status = root.find('overall_status').text
        clinicalSerachModel.start_date = root.find('start_date').text
        clinicalSerachModel.completion_date = root.find('completion_date')

        # clinicalSerachModel.start_date = datetime.datetime.strptime(root.find('start_date').text, "%B %Y").date()
        # clinicalSerachModel.completion_date = datetime.datetime.strptime(root.find('completion_date').text, "%B %Y").date()



        # insert sponsor
        for data in root.findall('sponsors'):
            for x in data.findall('lead_sponsor'):
                agency = x.find('agency').text
                agency_class=x.find('agency_class').text
                clinicalSerachModel.lead_sponsor_agency = agency
                clinicalSerachModel.lead_sponsor_agency_class = agency_class

        # insert brief textblock
        for data in root.findall('brief_summary'):
            textblock = data.find('textblock').text
            clinicalSerachModel.brief_summary = textblock

        # insert description textblock
        for data in root.findall('detailed_description'):
            clinicalSerachModel.brief_summary = data.find('textblock').text

        clinicalSerachModel.save()

        #insert primary outcomes and secondary outcome
        c = get_object_or_404(ClinicalStudy, pk=clinicalSerachModel.pk)
        for data in root.findall('primary_outcome'):
            c.outcome_set.create(outcome_type="primary_outcome", measure=data.find('measure').text, timeFrame=data.find('time_frame').text, description=data.find('description').text)

        for data in root.findall('secondary_outcome'):
            c.outcome_set.create(outcome_type="secondary_outcome", measure=data.find('measure').text, timeFrame=data.find('time_frame').text, description=data.find('description').text)

        # insert primary outcomes and secondary outcome
        for data in root.findall('condition'):
            c.condition_set.create(condition_name=data.text)

        context = {}
        return HttpResponse(template.render(context, request))
